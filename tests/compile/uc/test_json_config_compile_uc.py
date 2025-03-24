import unittest
from tools3 import Caller
from tools3.compile.uc import JsonConfigCompileUC

class TestJsonConfigCompileUC(unittest.TestCase):
    def test_compile(self):
        caller = Caller()
        load_json_file_path = caller.get_caller_filepath("_config.json", level=1)
        c = JsonConfigCompileUC(load_json_file_path)
        json_file_path = load_json_file_path.replace("_config.json", "_cases.json")
        result = c.compile(json_file_path)
        self.assertTrue(result)