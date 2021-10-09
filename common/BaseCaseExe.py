from common.BaseYamlParams import Params
from common.BaseYamlUtil import ReadYaml
from common.MemoryCase import MemoryCase


class DataManager(object):
    @staticmethod
    def yamlvalue(path):
        yaml_value = ReadYaml(path).read_yaml()
        return yaml_value


class Runcase(DataManager):
    def __init__(self):
        pass

    @staticmethod
    def case(path):
        yaml_value = Runcase.yamlvalue(path)
        run_case = Params(yaml_value).yaml_params_case()

        return run_case

    # 执行单个测试用例
    @staticmethod
    def run(value, case):
        # 前置
        Params(value).yaml_index_setup(case)
        # 执行
        Params(value).yaml_params_split(case)
        # 后置
        Params(value).yaml_index_teardown(case)

    def all_run(self, path, case):
        value = Runcase.yamlvalue(path)
        MemoryCase().add_memory_case_path(path)
        # 前置
        Params(value).yaml_setup()
        # 执行测试用例
        self.run(value, case)
        # 后置
        Params(value).yaml_teardown()
