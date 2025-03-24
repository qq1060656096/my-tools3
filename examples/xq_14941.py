from tools3.compile.uc import uc_gen_cases
from tools3 import Caller

# 定义参数
fields = {
    "can_use_integral": [None, "", "0", "1", "2"],
    "can_use_rebate": [None, "", "0", "1", "2"],
    "enable_integral": [None, "T", "F", "E"],
    "enable_rebate": [None, "T", "F", "E"],
}

# 用户自定义参数值格式化规则
fields_formatters = {
    "can_use_integral": {
        "format": "default",
        "values": {
            None: "积分_null",
            "": "积分_空字符串",
            "0": "积分_数字零",
            "1": "积分_是",
            "2": "积分_否",
        }
    },
    "can_use_rebate": {
        "format": "default",
        "values": {
            None: "返利_null",
            "": "返利_空字符串",
            "0": "返利_数字零",
            "1": "返利_是",
            "2": "返利_否",
        }
    },
    "enable_integral": {
        "format": "default",
        "values": {
            None: "积分应用未安装",
            "T": "积分应用已启用",
            "F": "积分应用禁用",
            "E": "积分应用已过期",
        }
    },
    "enable_rebate": {
        "format": "default",
        "values": {
            None: "返利应用未安装",
            "T": "返利应用已启用",
            "F": "返利应用禁用",
            "E": "返利应用已过期",
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
    if case_data["enable_integral"] == "T" or case_data["enable_rebate"] == "T":
        return {
            "hasException": True,
        }
    else:
        return {
            "hasException": True,
        }

# 生成测试用例
caller = Caller()
json_file_path = caller.get_caller_filepath(".json")
output_file_path = ""
if output_file_path !="":
    json_file_path = output_file_path
uc_gen_cases(
    json_file_path,
    fields=fields,
    fields_formatters=fields_formatters,
    expected=dynamic_expected,  # 传入动态生成函数
    include_field_names=False,
    separator="_",
)


