"""
    读取用例
"""
import os
from public.yaml.yamlParams import Params


class ReadCase(object):
    def __init__(self, path):
        self.path = path

    def readcase(self):
        if not os.path.exists(self.path):
            Exception("测试用例路径不存在："+self.path)
        CASE = Params(self.path).yaml_params_first()
        return CASE
