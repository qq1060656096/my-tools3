### tools3 工具安装

```text
1. 安装 tools3
2. 创建 jc 文件用于生成测试方法参数集合【示例 demo_config.json】
3. 安装php
4. 要测试的php文件【php业务代码文件】
5. 生成phpunit测试文件
6. 安装allure
7. pc-dhb168项目运行phpunit
8. 查看allure测试报告
```

## 1. 安装 tools3
```shell
python3 -m venv myenv
source myenv/bin/activate
pip install tools3==0.1.1 
pip install tools3==0.1.1 --index-url https://pypi.org/simple

```

## 2. 创建 jc 文件用于生成测试方法参数集合【示例 demo_config.json】

> vi demo_config.json
```json
{
  "params": {
    "list": {
      "values": {
        "list_null": null,
        "list_空字符串": "",
        "list_数组": []
      }
    },
    "brandList": {
      "values": {
        "brandList_null": null,
        "brandList_数组": []
      }
    },
    "companyId": {
      "values": {
        "公司id_null": null,
        "公司id_数字零": "0",
        "公司id_字符串": "631"
      }
    }
  },
  "expected": {
    "hasException": false,
    "code": [422, 500]
  }
}
```


## 3. 安装php
```shell
# ubuntu
sudo apt install software-properties-common -y
sudo add-apt-repository ppa:ondrej/php -y
sudo apt update
sudo apt install php7.3 -y
```

## 4. 要测试的php文件【php业务代码文件】
```shell
vi SetListOriginBrandInfo.php
```
```php
<?php
//  SetListOriginBrandInfo.php 文件内容
namespace Common\Modules\Infrastructure\Helper;

use Common\Modules\Goods\Domain\Repository\GoodsBrandRepository;

class SetListOriginBrandInfo extends SetListOriginRelationInfo
{
    /**
     * @var string 原始信息字段
     */
    protected $originInfoField = 'origin_brand_info';

    /**
     * @var array 原始信息列表主键字段
     */
    protected $originListPrimaryKeyFields = ['brand_id'];

    protected $setFields = [];

    /**
     * @return $this
     */
    public function setDefaultSetFields() {
        $this->addSetField('brand_name', '')
            ->addSetField('brand_num', '');
        return $this;
    }

    /**
     * 设置订单明细默认场景的商品信息
     *
     * @param array $list
     * @param array $brandList
     * @return void
     */
    public function listSet(&$list, $brandList = null, $companyId = null) {
        if ($list && is_null($brandList)) {
            if (is_null($companyId)) {
                $companyId = get_company_id();
            }
            $brandIds = array_column($list, 'brand_id');
            $brandIds = ArrayHelper::idsArrayDeleteValue($brandIds, null, '');
            $brandList  = (new GoodsBrandRepository())->getList($companyId, $brandIds);
        }
        $setListOriginGoodsInfo = new static();
        $setListOriginGoodsInfo->setDefaultSetFields();
        $setListOriginGoodsInfo->setList($list, $brandList);
    }

}
```


## 5. 生成phpunit测试文件
```shell
# 会在 demo_config.json 文件目录生成 demo_config.phpunit文件
tools3-cli -t jc_phpunit demo_config.json

# -o 生成phpunit到指定的文件 TestSetListOriginBrandInfo.php 
# 注意 -o 不会创建目录
tools3-cli -t jc_phpunit -php=/usr/bin/php -lt deepseek -lurl=https://api.deepseek.com -lk=sk-05e8317ce08641c684108e5012c560ec -lm=deepseek-chat -uf=SetListOriginBrandInfo.php -um=listSet -o TestSetListOriginBrandInfo.php demo_config.json
```

## 6. 安装allure
```shell
# 安装allure
sudo apt install allure -y
```

## 7. pc-dhb168项目运行phpunit
> 请切换到分支：phpunit-master
```shell
/usr/local/Cellar/php@7.3/7.3.33_11/bin/php -c .user2.ini build/phpunit -c phpunit.allure.xml tests/Tools3Tests/Dinghuobao/DhbApi/Controller/Admin/AdminBaseController/CheckURLRuleTest.php
```

## 8. 查看allure测试报告
```shell

allure serve tests/Tools3Tests/allure-results
```

### 安装报错
> pip install tools3=0.1.0.dev2 --index-url https://pypi.org/simple
```shell
INFO: pip is looking at multiple versions of langchain-community to determine which version is compatible with other requirements. This could take a while.
ERROR: Could not find a version that satisfies the requirement SQLAlchemy<3,>=1.4 (from langchain-community) (from versions: none)
ERROR: No matching distribution found for SQLAlchemy<3,>=1.4
```
> 解决办法
```shell
pip install --upgrade pip
```
> 解决办法2
```shell
pip install SQLAlchemy>=1.4,<3 --index-url https://pypi.org/simple
```