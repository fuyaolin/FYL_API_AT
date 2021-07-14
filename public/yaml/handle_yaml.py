from public.yaml.read_yaml import ReadYaml
from public.read_path import TESTCASE_YAML_PATH_test_01


class Params(object):
    def __init__(self,yaml_path):
        self.params = ReadYaml(yaml_path).read_yaml()

    def yaml_params(self):
        all_skip = self.params['all_skip']
        order_by = self.params['order_by']
        # # 此用例是否跳过，bool类型true为1
        if all_skip == 1:
            return 0
        # 此用例不跳过，而且没有执行顺序，按照从上到下的顺序执行
        elif all_skip != 1 and order_by == []:
            for index in self.params:
                if 'Case' in index:
                    order_by.append(index)
        # 此用例不跳过，有执行顺序，按照执行顺序执行
        for index in range(len(order_by)):
            case = order_by[index]
            self.case_params(case)

    def case_params(self, case):
        name = self.params[case]['name']
        title = self.params[case]['title']
        url = self.params[case]['request']['url']
        method = self.params[case]['request']['method']
        headers = self.params[case]['request']['headers']
        body = self.params[case]['request']['body']
        check = self.params[case]['request']['check']
        return name, title, url, method, headers, body, check
