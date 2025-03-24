import unittest

from tools3 import Caller
from tools3.compile.utc import UCCompilePhpUnit
from tools3.compile.codep import PhpParser

class TestUCCompilePhpUnit(unittest.TestCase):
    def test_compile(self):
        caller = Caller()

        parser = PhpParser("")
        code = parser.get_units_code("del")
        from_uc_file_path = caller.get_caller_filepath(".uc.json", level=1)
        to_utc_file_path = from_uc_file_path.replace(".uc.json", ".utc.php")
        uc_to_utc = UCCompilePhpUnit()
        uc_to_utc.set_template(code)
        result = uc_to_utc.compile(from_uc_file_path, to_utc_file_path)
        self.assertTrue(result)