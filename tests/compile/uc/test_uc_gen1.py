import unittest

from tools3 import Caller
from tools3.compile.uc import UCGen1


class TestUcGen1(unittest.TestCase):
    def test_ok(self):
        fields = {
            "can_use_integral": {
                "format": "default",
                "values": {
                    "积分_数组": [
                        "1",
                        "2",
                        "3"
                    ],
                    "积分_null": None,
                    "积分_空字符串": "",
                    "积分_数字零": "0",
                    "积分_是": "1",
                    "积分_否": "2"
                }
            },
            "can_use_rebate": {
                "format": "default",
                "values": {
                    "返利_null": None,
                    "返利_空字符串": "",
                    "返利_数字零": "0",
                    "返利_是": "1",
                    "返利_否": "2"
                }
            },
            "enable_integral": {
                "format": "default",
                "values": {
                    "积分应用未安装": None,
                    "积分应用已启用": "T",
                    "积分应用禁用": "F",
                    "积分应用已过期": "E"
                }
            },
            "enable_rebate": {
                "format": "default",
                "values": {
                    "返利应用未安装": None,
                    "返利应用已启用": "T",
                    "返利应用禁用": "F",
                    "返利应用已过期": "E"
                }
            }
        }
        ucg = UCGen1(fields = fields, expected=None)
        ucg.generate_cases()
        caller = Caller()
        save_json_file_path = caller.get_caller_filepath(".uc.json", level=1)
        ucg.save_to_json(save_json_file_path)

