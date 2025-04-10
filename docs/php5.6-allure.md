```shell
COMPOSER_MEMORY_LIMIT=-1 /usr/local/Cellar/php@5.6/5.6.40_12/bin/php build/composer.phar require --dev allure-framework/allure-php-api:~1.1.0 --ignore-platform-reqs
 
 COMPOSER_MEMORY_LIMIT=-1 /usr/local/Cellar/php@5.6/5.6.40_12/bin/php build/composer.phar dump-autoload -o
 
/usr/local/Cellar/php@7.3/7.3.33_11/bin/php -c .user2.ini build/phpunit -c tests/Tools3Tests/phpunit.allure.xml tests/Tools3Tests/Dinghuobao/DhbApi/Controller/Admin

allure serve build/allure-results
```


```php
<?php
namespace Tests\Tools3Tests;

use Exception;
use PHPUnit\Framework\AssertionFailedError;
use PHPUnit\Framework\ExpectationFailedException;
use PHPUnit\Framework\Test;
use PHPUnit\Framework\TestCase;
use PHPUnit\Framework\TestListener;
use PHPUnit\Framework\TestSuite;
use PHPUnit\Framework\DataProviderTestSuite;
use PHPUnit\Framework\Warning;
use Yandex\Allure\Adapter\Annotation;
use Yandex\Allure\Adapter\Event\TestCaseBrokenEvent;
use Yandex\Allure\Adapter\Event\TestCaseCanceledEvent;
use Yandex\Allure\Adapter\Event\TestCaseFailedEvent;
use Yandex\Allure\Adapter\Event\TestCaseFinishedEvent;
use Yandex\Allure\Adapter\Event\TestCasePendingEvent;
use Yandex\Allure\Adapter\Event\TestCaseStartedEvent;
use Yandex\Allure\Adapter\Event\TestSuiteFinishedEvent;
use Yandex\Allure\Adapter\Event\TestSuiteStartedEvent;
use Yandex\Allure\Adapter\Model;

class AllureAdapter implements TestListener
{

    //NOTE: here we implicitly assume that PHPUnit runs in single-threaded mode
    private $uuid;
    private $suiteName;
    private $methodName;

    /**
     * Annotations that should be ignored by the annotations parser (especially PHPUnit annotations)
     * @var array
     */
    private $ignoredAnnotations = [
        'after', 'afterClass', 'backupGlobals', 'backupStaticAttributes', 'before', 'beforeClass',
        'codeCoverageIgnore', 'codeCoverageIgnoreStart', 'codeCoverageIgnoreEnd', 'covers',
        'coversDefaultClass', 'coversNothing', 'dataProvider', 'depends', 'expectedException',
        'expectedExceptionCode', 'expectedExceptionMessage', 'group', 'large', 'medium',
        'preserveGlobalState', 'requires', 'runTestsInSeparateProcesses', 'runInSeparateProcess',
        'small', 'test', 'testdox', 'ticket', 'uses',
    ];

    /**
     * @param string $outputDirectory XML files output directory
     * @param bool $deletePreviousResults Whether to delete previous results on return
     * @param array $ignoredAnnotations Extra annotations to ignore in addition to standard PHPUnit annotations
     */
    public function __construct(
        $outputDirectory,
        $deletePreviousResults = false,
        array $ignoredAnnotations = []
    ) {
        if (!isset($outputDirectory)){
            $outputDirectory = 'build' . DIRECTORY_SEPARATOR . 'allure-results';
        }

        $this->prepareOutputDirectory($outputDirectory, $deletePreviousResults);

        // Add standard PHPUnit annotations
        Annotation\AnnotationProvider::addIgnoredAnnotations($this->ignoredAnnotations);
        // Add custom ignored annotations
        Annotation\AnnotationProvider::addIgnoredAnnotations($ignoredAnnotations);
    }

    public function prepareOutputDirectory($outputDirectory, $deletePreviousResults)
    {
        if (!file_exists($outputDirectory)) {
            mkdir($outputDirectory, 0755, true);
        }
        if ($deletePreviousResults) {
            $files = glob($outputDirectory . DIRECTORY_SEPARATOR . '{,.}*', GLOB_BRACE);
            foreach ($files as $file) {
                if (is_file($file)) {
                    unlink($file);
                }
            }
        }
        if (is_null(Model\Provider::getOutputDirectory())) {
            Model\Provider::setOutputDirectory($outputDirectory);
        }
    }

    /**
     * An error occurred.
     *
     * @param Test $test
     * @param Exception $e
     * @param float $time
     */
    public function addError(Test $test, \Throwable $e, float $time): void
    {
        $event = new TestCaseBrokenEvent();
        Allure::lifecycle()->fire($event->withException($e)->withMessage($e->getMessage()));
    }

    /**
     * A warning occurred.
     *
     * @param \PHPUnit\Framework\Test $test
     * @param \PHPUnit\Framework\Warning $e
     * @param float $time
     */
    public function addWarning(Test $test, Warning $e, float $time): void
    {
        // TODO: Implement addWarning() method.
    }

    /**
     * A failure occurred.
     *
     * @param Test $test
     * @param AssertionFailedError $e
     * @param float $time
     */
    public function addFailure(Test $test, AssertionFailedError $e, float $time): void
    {
        $event = new TestCaseFailedEvent();

        $message = $e->getMessage();

        // Append comparison diff for errors of type ExpectationFailedException (and is subclasses)
        if (($e instanceof ExpectationFailedException
                || is_subclass_of($e, 'PHPUnit\Framework\ExpectationFailedException'))
            && $e->getComparisonFailure()
        ) {
            $message .= $e->getComparisonFailure()->getDiff();
        }

        Allure::lifecycle()->fire($event->withException($e)->withMessage($message));
    }

    /**
     * Incomplete test.
     *
     * @param Test $test
     * @param Exception $e
     * @param float $time
     */
    public function addIncompleteTest(Test $test, \Throwable $e, float $time): void
    {
        $event = new TestCasePendingEvent();
        Allure::lifecycle()->fire($event->withException($e));
    }

    /**
     * Risky test.
     *
     * @param Test $test
     * @param Exception $e
     * @param float $time
     * @since  Method available since Release 4.0.0
     */
    public function addRiskyTest(Test $test, \Throwable $e, float $time): void
    {
        $this->addIncompleteTest($test, $e, $time);
    }

    /**
     * Skipped test.
     *
     * @param Test $test
     * @param Exception $e
     * @param float $time
     * @since  Method available since Release 3.0.0
     */
    public function addSkippedTest(Test $test, \Throwable $e, float $time): void
    {
        $shouldCreateStartStopEvents = false;
        if ($test instanceof TestCase){
            $methodName = $test->getName();
            if ($methodName !== $this->methodName){
                $shouldCreateStartStopEvents = true;
                $this->startTest($test);
            }
        }

        $event = new TestCaseCanceledEvent();
        Allure::lifecycle()->fire($event->withException($e)->withMessage($e->getMessage()));

        if ($shouldCreateStartStopEvents && $test instanceof TestCase){
            $this->endTest($test, 0);
        }
    }

    /**
     * A test suite started.
     *
     * @param TestSuite $suite
     * @since  Method available since Release 2.2.0
     */
    public function startTestSuite(TestSuite $suite): void
    {
        if ($suite instanceof DataProviderTestSuite) {
            return;
        }

        $suiteName = $suite->getName();
        $event = new TestSuiteStartedEvent($suiteName);
        $this->uuid = $event->getUuid();
        $this->suiteName = $suiteName;

        if (class_exists($suiteName, false)) {
            $annotationManager = new Annotation\AnnotationManager(
                Annotation\AnnotationProvider::getClassAnnotations($suiteName)
            );
            $annotationManager->updateTestSuiteEvent($event);
        }

        Allure::lifecycle()->fire($event);
    }

    /**
     * A test suite ended.
     *
     * @param TestSuite $suite
     * @since  Method available since Release 2.2.0
     */
    public function endTestSuite(TestSuite $suite): void
    {
        if ($suite instanceof DataProviderTestSuite) {
            return;
        }

        Allure::lifecycle()->fire(new TestSuiteFinishedEvent($this->uuid));
    }

    /**
     * A test started.
     *
     * @param Test $test
     */
    public function startTest(Test $test): void
    {
        if ($test instanceof TestCase) {
            $testName = $test->getName();
            $methodName = $this->methodName = $test->getName(false);

            $event = new TestCaseStartedEvent($this->uuid, $testName);
            if (method_exists($test, $methodName)) {
                $annotationManager = new Annotation\AnnotationManager(
                    Annotation\AnnotationProvider::getMethodAnnotations(get_class($test), $methodName)
                );
                $annotationManager->updateTestCaseEvent($event);
            }
            Allure::lifecycle()->fire($event);
        }
    }

    /**
     * A test ended.
     *
     * @param Test $test
     * @param float $time
     * @throws \Exception
     */
    public function endTest(Test $test, float $time): void
    {
        if ($test instanceof TestCase) {
            Allure::lifecycle()->fire(new TestCaseFinishedEvent());
        }
    }
}
```

