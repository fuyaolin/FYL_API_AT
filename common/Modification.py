"""
    参数化
"""
import re
from jsonpath import jsonpath
from common.Memory_Case import MemoryCase


def replace_link(link, alias, data):
    all_ready_case = MemoryCase().memory_case_param()
    alias = f'${alias}$'
    if len(data) < 0 or len(data) > 3:
        return False
    data_value = data['case']
    # 替换值
    select_key = f'$..{data_value}'
    ready_case_value = jsonpath(all_ready_case, select_key)[0]
    for data_key, data_value in data.items():
        replace_data = None
        data_type = 'str'
        if data_key == ('headers' or 'request' or 'response'):
            ready_value = jsonpath(ready_case_value, f'$..{data_key}')[0]
            replace_data = jsonpath(ready_value, f'$..{data_value}')[0]
        elif data_key == 'type':
            data_type = data['type']
        else:
            return False
        # 处理别名
        replace_data = type_change(replace_data, data_type)
        pattern = re.compile(r'\$.*?\$')
        result = pattern.findall(link)
        for i in result:
            if i == alias:
                link.replace(alias, replace_data)
    return link


def type_change(replace_data, data_type):
    if data_type == 'dict':
        return eval(replace_data)
    elif data_type == 'int':
        return int(replace_data)
    elif data_type == 'float':
        return float(replace_data)
    elif data_type == 'list':
        return list(replace_data)
    else:
        return str(replace_data)
