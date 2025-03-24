import unittest

from tools3 import Caller


class TestParamsJsonConfig(unittest.TestCase):
    def test_new_instance(self):
        from tools3.compile.config import ParamsJsonConfig
        caller = Caller()
        json_file_path = caller.get_caller_filepath(".json", level= 1)
        params_json_config = ParamsJsonConfig.new_instance(json_file_path)
        self.assertEqual(params_json_config.get_name(), "test_params_json_config")