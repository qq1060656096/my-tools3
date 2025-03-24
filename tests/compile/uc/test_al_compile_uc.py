import unittest

from tools3 import Caller
from tools3.compile.uc import AlCompileUC


class TestALCompileUC(unittest.TestCase):
    def test_compile(self):
        # TODO: Add test cases
        self.assertTrue(True)
        caller = Caller()
        uc_json_file_path = caller.get_caller_filepath(".uc.json", level=1)
        al = AlCompileUC("test.json")
        result = al.compile(uc_json_file_path)
        self.assertTrue(True)