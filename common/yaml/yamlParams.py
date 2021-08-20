"""
    解读yaml参数
"""
from common.log import Logger
import pytest


class Params(object):
    def __init__(self, yaml_values):
        self.params = yaml_values
        self.runcase = []
        self.all_skip = False
        self.order_by = []
        # self.skip = None
        # self.url = None
        # self.method = None
        # self.headers = None
        # self.json_body = None
        # self.name = None
        # self.title = None
        # self.check = Nones

    # 处理yaml文件内容,返回执行顺序参数
    def yaml_params_case(self):
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
        Logger().logs_file().debug("执行用例顺序为：" + str(self.runcase))
        return self.runcase

    # 测试用例接口参数
    def yaml_params_split(self, index):
        if self.params['testcase'][index]['skip']:
            self.skip = self.params['testcase'][index]['skip']
            if self.skip == 1:
                pytest.skip("测试用例开关未开启")
                Logger().logs_file().debug(str(index) + "测试用例开关未开启")
            else:
                assert 1 == 1
    #     if self.params['testcase'][index]['request']['url']:
    #         if ReadConfig().get_url is not None:
    #             self.url = ReadConfig().get_url + self.params['testcase'][index]['request']['url']
    #         else:
    #             self.url = self.params['testcase'][index]['request']['url']
    #     if self.params['testcase'][index]['request']['method']:
    #         self.method = self.params['testcase'][index]['request']['method']
    #     if self.params['testcase'][index]['request']['headers']:
    #         self.headers = self.params['testcase'][index]['request']['headers']
    #     if self.params['testcase'][index]['request']['body']:
    #         self.json_body = self.params['testcase'][index]['request']['body']
    #     # self.name = self.params['testcase'][index]['name']
    #     # self.title = self.params['testcase'][index]['title']
    #     if self.params['testcase'][index]['request']['check']:
    #         self.check = self.params['testcase'][index]['request']['check']
