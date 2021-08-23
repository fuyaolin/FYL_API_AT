from common.yamlParams import Params
from common.yamlUtil import ReadYaml


class DataManager(object):
    def __init__(self):
        pass

    @staticmethod
    def yamlvalue(path):
        yaml_value = ReadYaml(path).read_yaml()
        return yaml_value

    @staticmethod
    def case(path):
        yaml_value = DataManager.yamlvalue(path)
        run_case = Params(yaml_value).yaml_params_case()
        return run_case

    @staticmethod
    def run(path, case):
        value = DataManager.yamlvalue(path)
        Params(value).yaml_params_split(case)
