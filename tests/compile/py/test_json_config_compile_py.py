import unittest

from tools3 import Caller
from tools3.compile.py import JsonConfigCompilePy
class TestJsonConfigCompilePy(unittest.TestCase):
    def test_compile(self):
        caller = Caller()
        json_file_path = caller.get_caller_filepath(".json", level=1)
        commpile_py = JsonConfigCompilePy(json_file_path)
        py_file_path = json_file_path + ".py"
        commpile_py.compile(py_file_path)