"""
    解读yaml参数
    现存问题：
            前后置如何执行？ 直接调用就可以
            参数如何关联？
            返回参数中文件下载和请求参数中的文件/图片上传？
            excel表格上传生成yaml文件？
            报告的生成？
            自动生成同名py文件？
            随机数什么的
"""
import pytest
from common.log import Logger
from common.read_config import ReadConfig
from common.request import YamlRequest
from common.prefixed import Prefixed


class Params(object):
    def __init__(self, yaml_values):
        self.params = yaml_values
        self.runcase = []
        self.all_skip = None
        self.order_by = []
        self.name = None
        self.title = None
        if 'headers' in self.params.keys():
            self.headers = self.params['headers']
        else:
            self.headers = None
        self.body = None
        self.url = None
        self.method = None
        self.check = None

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

    def yaml_setup(self):
        if self.params['all_skip'] != 1 and 'setup' in self.params.keys():
            Prefixed().exe_prefixed()

    def yaml_teardown(self):
        if self.params['all_skip'] != 1 and 'teardown' in self.params.keys():
            Prefixed().exe_suffixed()

    def yaml_index_setup(self, index):
        if self.params['testcase'][index]['setup']:
            Prefixed().exe_prefixed()

    def yaml_index_teardown(self, index):
        if self.params['testcase'][index]['teardown']:
            Prefixed().exe_suffixed()

    # 测试用例接口参数
    def yaml_params_split(self, index):
        # 单个用例是否跳过,此参数必须存在
        if self.params['testcase'][index]['skip']:
            skip = self.params['testcase'][index]['skip']
            if skip == 1:
                pytest.skip("测试用例开关未开启")
                Logger().logs_file().debug(str(index) + "测试用例开关未开启")
        # 此参数必须存在
        if self.params['testcase'][index]['name']:
            self.name = self.params['testcase'][index]['name']
        if self.params['testcase'][index]['title']:
            self.title = self.params['testcase'][index]['title']
        # 请求头参数，可不存在
        if "header" in self.params['testcase'][index]['request'].keys():
            self.headers = self.params['testcase'][index]['request']['header']
        # 请求url，必须存在
        if self.params['testcase'][index]['request']['url']:
            url = self.params['testcase'][index]['request']['url']
            if url[:1] is "/":
                self.url = ReadConfig().get_url + url
            else:
                self.url = url
        else:
            pytest.xfail(reason="name:"+self.name+",title:"+self.title+"请加入请求地址url参数")
        # 请求方法，不可为空
        if self.params['testcase'][index]['request']['method']:
            self.method = self.params['testcase'][index]['request']['method']
        else:
            pytest.xfail(reason="name:"+self.name+",title:"+self.title+"请加入请求方法method参数")
        # 请求body,可不存在
        if "body" in self.params['testcase'][index]['request'].keys():
            self.body = self.params['testcase'][index]['request']['body']
        # 预期结果,可不存在
        if 'check' in self.params['testcase'][index].keys():
            self.check = self.params['testcase'][index]['check']
        Logger().logs_file().debug("name:"+str(self.name)+",title:"+str(self.title))

        YamlRequest(index=index, url=self.url, method=self.method, headers=self.headers,
                    body=self.body, check=self.check).yaml_request()
