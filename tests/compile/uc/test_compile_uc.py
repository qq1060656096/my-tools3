import unittest
from tools3 import Caller
from tools3.compile.uc import CompileUC

class TestCompileUC(unittest.TestCase):
    def test_compile_json_use_cases(self):
        # 定义参数
        params = {
            "can_use_integral": [None, "", "0", "1", "2"],
            "enable_integral": [None, "T", "F", "E"],
        }

        # 用户自定义参数值格式化规则
        value_formatters = {
            "can_use_integral": {
                "format": "default",
                "values": {
                    None: "积分_null",
                    "": "积分_空字符串",
                    "0": "积分_数字零",
                    "1": "积分_是",
                    "2": "积分_否",
                }
            },
            "enable_integral": {
                "format": "default",
                "values": {
                    None: "积分应用未安装",
                    "T": "积分应用已启用",
                    "F": "积分应用禁用",
                    "E": "积分应用已过期",
                }
            }
        }

        # 定义预期结果（可以是固定值或动态生成函数）
        def dynamic_expected(case_data):
            return {
                "isInit": True,
            }
        c = CompileUC(
            params,
            value_formatters,
            dynamic_expected,
            include_field_names=False,
            separator="_",
        )
        caller = Caller()
        json_file_path = caller.get_caller_filepath("_cases.json", level=1)
        result = c.compile(json_file_path)
        self.assertTrue(result)