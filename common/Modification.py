"""
    参数化
"""
import re
from jsonpath import jsonpath
from common.Memory_Case import MemoryCase


class Link(object):
    def __init__(self):
        self.link = ""
        self.new_replace_data = ""

    def replace_link(self, link, alias, data):
        self.link = str(link)
        all_ready_case = MemoryCase().memory_case_param()
        alias = f'${alias}$'
        if len(data) < 0 or len(data) > 3:
            return False
        data_value = data['case']
        # 替换值
        select_key = f'$..case.{data_value}'
        if jsonpath(all_ready_case, select_key):
            ready_case_value = jsonpath(all_ready_case, select_key)[0]

            for data_key, data_value in data.items():
                replace_data = None
                if data_key == 'case':
                    continue
                elif data_key in ['headers', 'request', 'response']:
                    if ready_case_value is not None and jsonpath(ready_case_value, f'$..{data_key}'):
                        ready_value = jsonpath(ready_case_value, f'$..{data_key}')[0]
                        if ready_value is not None and jsonpath(ready_value, f'$..{data_value}'):
                            replace_data = jsonpath(ready_value, f'$..{data_value}')[0]
                elif data_key == 'type':
                    data_type = data['type']
                else:
                    return False
                if not isinstance(replace_data, str):
                    self.new_replace_data = '{replace_data}'.format(replace_data=replace_data)
                pattern = re.compile(r'\$.*?\$')
                result = pattern.findall(self.link)
                for i in result:
                    if i == alias:
                        self.link = str(self.link).replace(alias, self.new_replace_data)
            return self.link