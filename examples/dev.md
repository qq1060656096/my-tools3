```text
http://project.dhb168.com/browse/TRACK-11741
http://project.dhb168.com/browse/TRACK-11768
http://project.dhb168.com/browse/TRACK-11775
http://project.dhb168.com/browse/TRACK-11779
```

```text
http://project.dhb168.com/browse/DHB-14941

之前我们写这种用例一个要1分钟
现在30秒

用了工具只5分钟
30秒 * 400
[
    'testcase' => '227_积分_数字零_返利_否_积分应用未安装_返利应用禁用',
    'data' => [
        'can_use_integral' => '0',
        'can_use_rebate' => '2',
        'enable_integral' => NULL,
        'enable_rebate' => 'F',
    ],
    'expected' => [
        'hasException' => false,
    ],
],

```