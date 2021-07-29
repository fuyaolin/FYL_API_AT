from public.yaml.yamlUtil import ReadYaml
from public.testcase_path import TESTCASE_YAML_TEST_01_PATH
from public.yaml.yamlManager import YamlRequest

class Params(object):
    def __init__(self, yaml_path):
        self.params = ReadYaml(yaml_path).read_yaml()

    # 处理yaml文件内容
    def yaml_params(self):
        all_skip = self.params['all_skip']
        order_by = self.params['order_by']
        # # 此用例是否跳过，bool类型true为1
        if all_skip == 1:
            return 0
        # 整个测试用例不跳过，而且没有执行顺序，按照从上到下的顺序执行
        elif all_skip != 1 and order_by == []:
            for index in self.params:
                if 'Case' in index:
                    order_by.append(index)
        # 整个测试用例不跳过，单个用例有执行顺序，按照执行顺序执行
        for index in range(len(order_by)):
            case = order_by[index]
            skip = self.params[case]['skip']
            # 单个测试用例跳过
            if skip == 1:
                continue
            else:
                self.case_params(case)

    # 测试用例接口参数
    def case_params(self, case):
        name = self.params[case]['name']
        title = self.params[case]['title']
        url = self.params[case]['request']['url']
        method = self.params[case]['request']['method']
        headers = self.params[case]['request']['headers']
        body = self.params[case]['request']['body']
        check = self.params[case]['request']['check']
        if method == ('get' or 'GET'):
            YamlRequest(headers, url, body, check).yaml_get()
        elif method == ('post' or 'POST'):
            YamlRequest(headers, url, body, check).yaml_post()
        elif method == ('put' or 'PUT'):
            YamlRequest(headers, url, body, check).yaml_put()
        elif method == ('delete' or 'DELETE'):
            YamlRequest(headers, url, body, check).yaml_delete()
        else:
            Exception('请输入正确的请求方法')

if __name__ == '__main__':
    Params(TESTCASE_YAML_TEST_01_PATH).yaml_params()
