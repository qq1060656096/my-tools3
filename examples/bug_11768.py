from tools3.compile.uc import uc_gen_cases
from tools3 import Caller

# 定义参数
fields = {
    "old_m_units": ["", "包"],
    "old_m_rate": ["0.0000", "1.0000", "2.0000", "5.0000"],
    "old_c_units": ["", "件"],
    "old_c_number": ["0.0000", "1.0000", "5.0000", "10.0000"],
    "new_m_units": ["", "包"],
    "new_m_rate": ["0.0000", "1.0000", "2.0000", "5.0000"],
    "new_c_units": ["", "件"],
    "new_c_number": ["0.0000", "1.0000", "5.0000", "10.0000"],
}


# 用户自定义参数值格式化规则
fields_formatters = {
    "old_m_units": {
        "format": "default",
        "values": {
            "": "商品无中单位名",
            "包": "商品有中单位名",
        }
    },
    "old_m_rate": {
        "format": "default",
        "values": {
            "0.0000": "商品无中单位换算关系",
            "1.0000": "商品有中单位换算关系1",
            "2.0000": "商品有中单位换算关系2",
            "5.0000": "商品有中单位换算关系5",
        }
    },
    "old_c_units": {
        "format": "default",
        "values": {
            "": "商品无大单位名",
            "件": "商品有大单位名",
        }
    },
    "old_c_number": {
        "format": "default",
        "values": {
            "0.0000": "商品无大单位数量",
            "1.0000": "商品有大单位数量1",
            "5.0000": "商品有大单位数量5",
            "10.0000": "商品有大单位数量10",
        }
    },
    "new_m_units": {
        "format": "default",
        "values": {
            "": "修改商品无中单位名",
            "包": "修改商品有中单位名",
        }
    },
    "new_m_rate": {
        "format": "default",
        "values": {
            "0.0000": "修改商品无中单位换算关系",
            "1.0000": "修改商品有中单位换算关系1",
            "2.0000": "修改商品有中单位换算关系2",
            "5.0000": "修改商品有中单位换算关系5",
        }
    },
    "new_c_units": {
        "format": "default",
        "values": {
            "": "修改商品无大单位名",
            "件": "修改商品有大单位名",
        }
    },
    "new_c_number": {
        "format": "default",
        "values": {
            "0.0000": "修改商品无大单位数量",
            "1.0000": "修改商品有大单位数量1",
            "5.0000": "修改商品有大单位数量5",
            "10.0000": "修改商品有大单位数量10",
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
    if case_data["new_c_number"] == "0.0000":
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
