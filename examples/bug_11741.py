from tools3.compile.uc import uc_gen_cases
from tools3 import Caller

# 定义参数
# 定义参数
fields = {
    "key": [None, "", "0", "table_result"],
    "vars": [
        None,
        """{"table_result": "clientNowPaySubmitOrderControl"}""",
        """{"table_result": "{\\"rawErrorOld\\":0}"}""",
        """{"table_result": ""}""",
        """{"table_result": null}""",
        """{"table_result": 0}""",
        """{"table_result": 123}""",
    ],
}

# 用户自定义参数值格式化规则
fields_formatters = {
    "key": {
        "format": "default",
        "values": {
            None: "key_null",
            "": "key_空字符串",
            "0": "key_数字零",
            "table_result": "key_有值",
        }
    },
    "vars": {
        "format": "default",
        "values": {
            None: "REQUEST没有值",
            """{"table_result": "clientNowPaySubmitOrderControl"}""": "REQUEST有table_result健并且有值",
            """{"table_result": "{\\"rawErrorOld\\":0}"}""": "REQUEST有table_result健并且有json值",
            """{"table_result": ""}""": "REQUEST有table_result健并且是空字符串",
            """{"table_result": null}""": "REQUEST有table_result健并且是null",
            """{"table_result": 0}""": "REQUEST有table_result健并且是0",
            """{"table_result": 123}""": "REQUEST有table_result健并且是123",
        }
    },
}


# 定义预期结果（可以是固定值或动态生成函数）
def dynamic_expected(case_data):
    """
    动态生成预期结果的函数
    :param case_data: 测试用例数据
    :return: 预期结果
    """
    if case_data["key"] == "table_result":
        return {
            "isBackup": True,
            "vars": case_data["vars"],
        }
    else:
        return {
            "isBackup": False,
            "vars": case_data["vars"],
        }


# 生成测试用例
caller = Caller()
json_file_path = caller.get_caller_filepath(".json")
uc_gen_cases(
    json_file_path,
    fields=fields,
    fields_formatters=fields_formatters,
    expected=dynamic_expected,  # 传入动态生成函数
    include_field_names=False,
    separator="_",
)
