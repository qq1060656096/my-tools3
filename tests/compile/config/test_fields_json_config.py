import unittest

from tools3 import Caller
from tools3.compile.config import FieldsJsonConfig


class TestParamsJsonConfig(unittest.TestCase):
    def test_new_instance(self):
        from tools3.compile.config import ParamsJsonConfig
        caller = Caller()
        json_file_path = caller.get_caller_filepath(".json", level= 1)
        fields_json_config = FieldsJsonConfig.new_instance(json_file_path)
        self.assertEqual(fields_json_config.get_name(), "test_fields_json_config")
        self.assertEqual(fields_json_config.get_fields(), {
            "can_use_integral": {
                "values": {
                    "积分_null": None,
                    "积分_空字符串": "",
                    "积分_数字零": "0",
                    "积分_是": "1",
                    "积分_否": "2"
                }
            },
            "enable_integral": {
                "values": {
                    "积分应用未安装": None,
                    "积分应用已启用": "T",
                    "积分应用禁用": "F",
                    "积分应用已过期": "E"
                }
            }
        })

        self.assertEqual(fields_json_config.get_expected(), {
            "hasException": False
        })
        self.assertEqual(fields_json_config.get_include_field_names(), True)
        self.assertEqual(fields_json_config.get_separator(), ';')