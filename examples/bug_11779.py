from tools3.compile.uc import uc_gen_cases
from tools3 import Caller

# 定义参数
fields = {
    "clearingForm": ["forward", "prepaid", "postpaid"],
    "clientNowPaySubmitOrderControl": ["T", "F"],
    "pay_status": [
        "oblig",
        "unoblig",
        "uncollect",
        "paided",
        "cancelled",
        "wait",
        "part",
    ],
    "pay_status_count": [0, 1],
}


# 用户自定义参数值格式化规则
fields_formatters = {
    "clearingForm": {
        "format": "default",
        "values": {
            "forward": "现付",  # 将 "forward" 映射为 "正向"
            "prepaid": "预付",  # 将 "prepaid" 映射为 "预付费"
            "postpaid": "后付",  # 将 "postpaid" 映射为 "后付费"
        }
    },
    "clientNowPaySubmitOrderControl": {
        "format": "default",
        "values": {
            "T": "启用",  # 将 "T" 映射为 "True"
            "F": "禁用",  # 将 "F" 映射为 "False"
        }
    },
    "pay_status": {
        "format": "default",
        "values": {
            "oblig": "待付款",  # 将 "oblig" 映射为 "待付款"
            "unoblig": "待核销",  # 将 "unoblig" 映射为 "待核销"
            "uncollect": "待收款",  # 将 "uncollect" 映射为 "待收款"
            "paided": "已付款",  # 将 "paided" 映射为 "已付款"
            "cancelled": "已取消",  # 将 "cancelled" 映射为 "已取消"
            "wait": "待确认",  # 将 "wait" 映射为 "待确认"
            "part": "部分确认",  # 将 "part" 映射为 "待处理"
        }
    },
    "pay_status_count": {
        "format": "default",
        "values": {
            0: "没有订单",
            1: "有订单"
        }
    }
}


# 定义预期结果（可以是固定值或动态生成函数）
def dynamic_expected(case_data):
    """
    动态生成预期结果的函数
    :param case_data: 测试用例数据
    :return: 预期结果
    """
    if case_data["pay_status"] == "paided" and case_data["pay_status_count"] == 1:
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

