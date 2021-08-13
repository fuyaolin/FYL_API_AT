"""
    解读yaml参数
"""
from common.yaml.yamlUtil import ReadYaml
from common.yaml.yamlRequest import YamlRequest


class Params(object):
    def __init__(self, yaml_path):
        self.runcase = []
        self.params = ReadYaml(yaml_path).read_yaml()
        self.all_skip = False
        self.order_by = []
        self.skip = False
        self.url = None
        self.method = None
        self.headers = None
        self.json_body = None
        self.name = None
        self.title = None
        self.check = None

    # 处理yaml文件内容
    def yaml_params_first(self):
        self.all_skip = self.params['all_skip']
        self.order_by = self.params['order_by']
        # # 此用例是否跳过，bool类型true为1
        if self.all_skip == 1:
            return self.runcase
        # 整个测试用例不跳过，而且没有执行顺序，按照从上到下的顺序执行
        elif self.all_skip != 1 and self.order_by == []:
            for case in self.params['testcase'].keys():
                self.order_by.append(case)
                self.runcase.append(case)
        # 整个测试用例不跳过，单个用例有执行顺序，按照执行顺序执行
        else:
            self.runcase = self.order_by
        return self.runcase

    # 测试用例接口参数
    def yaml_params_second(self, index):
        # for index in case:
        self.skip = self.params['testcase'][index]['skip']
        if self.skip == 1:
            return 0
        self.url = self.params['testcase'][index]['request']['url']
        self.method = self.params['testcase'][index]['request']['method']
        self.headers = self.params['testcase'][index]['request']['headers']
        self.json_body = self.params['testcase'][index]['request']['body']
        # self.name = self.params['testcase'][index]['name']
        # self.title = self.params['testcase'][index]['title']
        self.check = self.params['testcase'][index]['request']['check']

        YamlRequest(method=self.method, headers=self.headers, url=self.url, json_body=self.json_body, check=self.check).yaml_request()