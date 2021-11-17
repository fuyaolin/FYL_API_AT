"""
    关联测试用例参数$$
"""
import re
from jsonpath import jsonpath
from common.MemoryCase import MemoryCase


class Link(object):
    def __init__(self):
        self.link = ""
        self.new_replace_data = ""

    def replace_link(self, link, alias, data):
        """
        :param link: 关联的前url/body
        :param alias: 别名
        :param data: 关联的内容，包括关联的用例,关联的位置（'headers', 'request', 'response'）,关联值的key
        :return: 关联后的url/body
        """
        self.link = str(link)
        # 获取当下的已执行的测试用例
        all_ready_case = MemoryCase().memory_case_param()
        alias = f'${alias}$'
        if len(data) < 1 or len(data) > 3:
            return False
        # 获取关联的测试用例下的值
        data_value = data['case']
        select_key = f'$..case.{data_value}'
        if jsonpath(all_ready_case, select_key):
            ready_case_value = jsonpath(all_ready_case, select_key)[0]
            for data_key, data_value in data.items():
                replace_data = None
                if data_key == 'case':
                    continue
                # 获取关联的位置
                elif data_key in ['headers', 'request', 'response']:
                    if ready_case_value is not None and jsonpath(ready_case_value, f'$..{data_key}'):
                        # 关联位置的具体值
                        ready_value = jsonpath(ready_case_value, f'$..{data_key}')[0]
                        if ready_value is not None and jsonpath(ready_value, f'$..{data_value}'):
                            # 关联位置的具体值下的key对应的value
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