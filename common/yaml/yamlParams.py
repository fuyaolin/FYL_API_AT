"""
    解读yaml参数
"""
from common.yaml.yamlUtil import ReadYaml
from common.yaml.yamlRequest import YamlRequest


class Params(object):
    def __init__(self, yaml_path):
        self.runcase = []
        self.params = ReadYaml(yaml_path).read_yaml()

    # 处理yaml文件内容
    def yaml_params_first(self):
        all_skip = self.params['all_skip']
        order_by = self.params['order_by']
        # # 此用例是否跳过，bool类型true为1
        if all_skip == 1:
            return self.runcase
        # 整个测试用例不跳过，而且没有执行顺序，按照从上到下的顺序执行
        elif all_skip != 1 and order_by == []:
            for case in self.params['testcase'].keys():
                self.params['order_by'].append(case)
                self.runcase.append(case)
        # 整个测试用例不跳过，单个用例有执行顺序，按照执行顺序执行
        else:
            self.runcase = self.params['order_by']
        return self.runcase

    # 测试用例接口参数
    def yaml_params_second(self, case):
        for index in case:
            skip = self.params['testcase'][index]['skip']
            if skip == 1:
                continue
            # if self.params['testcase'][index]['request']['url'] is not None:
            url = self.params['testcase'][index]['request']['url']
            method = self.params['testcase'][index]['request']['method']
            headers = self.params['testcase'][index]['request']['headers']
            json_body = self.params['testcase'][index]['request']['body']
            # name = self.params['testcase'][index]['name']
            # title = self.params['testcase'][index]['title']
            check = self.params['testcase'][index]['request']['check']

            YamlRequest(method=method, headers=headers, url=url, json_body=json_body, check=check).yaml_request()