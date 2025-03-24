from tools3.compile.uc import uc_gen_cases
from tools3 import Caller

# 定义参数
fields = {
    "company_id": ["243037"],
    "version": ["affiliate", "free", "professional", "collaborate", "ultimate", "professional_new", "fresh", "catering"],
    "hasInfo": [0, 1],
}
# 用户自定义参数值格式化规则
fields_formatters = {
    "company_id": {
        "format": "default",
        "values": {
            "243037": "公司243037",
        }
    },
    "version": {
        "format": "default",
        "values": {
            "affiliate": "联营版",
            "free": "免费版",
            "professional": "专业版",
            "collaborate": "联营平台版",
            "ultimate": "旗舰版",
            "professional_new": "新专业版",
            "fresh": "生鲜版",
            "catering": "餐饮版"
        }
    },
    "hasInfo": {
        "format": "default",
        "values": {
            0: "有序号",
            1: "没有序号"
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
    if case_data["hasInfo"] == 0:
        return {"isInit": True}
    else:
        return {"isInit": False}


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