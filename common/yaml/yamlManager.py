"""
    读取用例
"""
import os
from common.yaml.yamlParams import Params


class ReadCase(object):
    def __init__(self, path):
        self.path = path

    def readcase(self):
        if not os.path.exists(self.path):
            Exception("测试用例路径不存在："+self.path)
        runcase = Params(self.path).yaml_params_first()
        return runcase
