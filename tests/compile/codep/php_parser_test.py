import unittest

from tools3.compile.codep import PhpParser

class PhpParserTest(unittest.TestCase):
    def test_get_method_code(self):
        parser = PhpParser("")
        method_code = parser.get_method_code("add")
        self.assertTrue(len(method_code) > 5)
        # parser.get_units_code("add")
        code = parser.get_units_code("del")
        self.assertTrue(len(code) > 5)
