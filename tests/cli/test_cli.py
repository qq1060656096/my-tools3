import os
import unittest
from tools3 import Caller, get_file_dir
from tools3.cli.cli import get_output_file_path
import allure


@allure.feature('命令行')
@allure.story('子功能')
class TestCli(unittest.TestCase):
    get_output_file_path_data_provider = [
        {
            "test_case": "只有from_file, output_file=None",
            "data": {
                "from_file": "test_cli.json",
                "output_file": None,
                "utc_file_ext": ".utc"
            },
            "expected": {
                "output_file": "test_cli.json.utc"
            }
        },
        {
            "test_case": "只有from_file, output_file=''",
            "data": {
                "from_file": "test_cli.json",
                "output_file": "",
                "utc_file_ext": ".utc"
            },
            "expected": {
                "output_file": "test_cli.json.utc"
            }
        },
        {
            "test_case": "只有from_file, output_file=存在的文件",
            "data": {
                "from_file": "test_cli.json",
                "output_file": "test_cli_output_file.uc",
                "utc_file_ext": ".utc"
            },
            "expected": {
                "output_file": "test_cli_output_file.uc"
            }
        },
        {
            "test_case": "只有from_file, output_file=是存在的目录",
            "data": {
                "from_file": "test_cli.json",
                "output_file": "test_cli_output_file",
                "utc_file_ext": ".utc"
            },
            "expected": {
                "output_file": "test_cli_output_file/test_cli.json.utc"
            }
        }
    ]
    def test_get_output_file_path(self):
        caller = Caller()
        file = caller.get_caller_filepath(".txt")
        dir = get_file_dir(file)
        dir = dir + "/"
        for test_case in self.get_output_file_path_data_provider:
            name = test_case["test_case"]
            data = test_case["data"]
            from_file = dir + data["from_file"]
            output_file = data["output_file"]
            if output_file is not None and output_file != "":
                output_file = dir + output_file
            utc_file_ext = data["utc_file_ext"]
            output_file2 = get_output_file_path(from_file, output_file, utc_file_ext)
            expected = test_case["expected"]
            expected["output_file"] = dir + expected["output_file"]
            self.assertEqual(expected["output_file"], output_file2, name)
