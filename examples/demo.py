from tools3.compile.uc import uc_gen_cases
from tools3 import Caller

# 定义参数
fields = {
    "arg1": ["a11", "a12"],
    "arg2": [None, "", "21", "22"],
}


# 用户自定义参数值格式化规则
fields_formatters = {
    "arg1": {
        "format": "default",
        "values": {
            "a11": "参数1_值1",
            "a12": "参数1_值2",
        }
    },
    "arg2": {
        "format": "default",
        "values": {
            None: "参数2_null",
            "": "参数2_空字符串",
            "21": "参数2_值3",
            "22": "参数3_值4",
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
    if case_data["arg1"] == "a11":
        return {"has": True}
    else:
        return {"has": False}



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

