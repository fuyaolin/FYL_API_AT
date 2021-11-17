"""
    函数参数化${文件名.函数名}$
"""
import re
import os
from common.ReadPath import REPLACE_FUNCTION_PATH
from common.UpdateLog import Logger


class ParameterSub(object):
    def __init__(self, params):
        self.params = params

    def substitution(self):
        if isinstance(self.params, dict):
            self.params =str(self.params)
        pattern = re.compile(r'\$\{.*?\}\$')
        result = pattern.findall(self.params)
        for fun_index in result:
            # 提取文件名.函数名
            fun = fun_index[2:-2]
            if len(fun.split('.')) < 2:
                continue
            fun_file = fun.split('.')[0]
            fun_path = os.path.join(REPLACE_FUNCTION_PATH, fun_file + '.py')
            if os.path.exists(fun_path):
                fun_name = fun[len(fun_file) + 1:]
                # 导入文件
                try:
                    exec(f"from public.function.{fun_file} import *")
                except ImportError:
                    Logger().logs_file().warning("{fun_name}替换参数失败,报错{e}".format(fun_name=fun_name, e=ImportError))
                    continue
                # 执行函数
                return_value = eval(fun_name)
                if return_value:
                    self.params = self.params.replace(fun_index, return_value)
        return eval(self.params)
