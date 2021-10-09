"""
    解读yaml参数
"""

import time
import pytest
import allure
from common.UpdateLog import Logger
from common.ReadConfigFile import ReadConfig
from common.BaseRequest import YamlRequest
from public.prefixed import Prefixed
from common.MemoryCase import MemoryCase
from common.Modification import Link


class Params(object):
    def __init__(self, yaml_values):
        self.params = yaml_values
        self.runcase = []
        self.all_skip = None
        self.order_by = []
        self.name = None
        self.title = None
        self.headers = self.params['headers'] if "headers" in self.params.keys() else None
        self.body = None
        self.url = None
        self.method = None
        self.file = None
        self.image = None
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
        Logger().logs_file().debug("执行用例顺序为：{runcase}".format(runcase=self.runcase))
        return self.runcase

    def yaml_setup(self):
        if 'setup' in self.params.keys() and self.params['all_skip'] != 1:
            prefixed_value = self.params['setup']
            Prefixed(prefixed_value).exe_prefixed()

    def yaml_teardown(self):
        if 'teardown' in self.params.keys() and self.params['all_skip'] != 1:
            teardown_value = self.params['teardown']
            Prefixed(teardown_value).exe_suffixed()

    def yaml_index_setup(self, index):
        if 'setup' in self.params['testcase'][index].keys() and self.params['testcase'][index]['skip'] != 1:
            prefixed_value = self.params['testcase'][index]['setup']
            Prefixed(prefixed_value).exe_prefixed()

    def yaml_index_teardown(self, index):
        if 'teardown' in self.params['testcase'][index].keys() and self.params['testcase'][index]['skip'] != 1:
            teardown_value = self.params['testcase'][index]['teardown']
            Prefixed(teardown_value).exe_suffixed()

    # 测试用例接口参数
    def yaml_params_split(self, index):
        # 单个用例是否跳过,此参数必须存在
        if self.params['testcase'][index]['skip']:
            skip = self.params['testcase'][index]['skip']
            if skip == 1:
                pytest.skip("测试用例开关未开启")
                Logger().logs_file().debug("{index} 测试用例开关未开启".format(index=index))

        # 休眠参数，可不存在
        if 'sleep' in self.params['testcase'][index].keys():
            sleep_time = self.params['testcase'][index]['sleep']
            time.sleep(sleep_time)

        # 此参数必须存在
        if self.params['testcase'][index]['name']:
            self.name = self.params['testcase'][index]['name']
            with allure.step('name'):
                allure.attach('name: {name}'.format(name=self.name), 'name')

        if self.params['testcase'][index]['title']:
            self.title = self.params['testcase'][index]['title']
            with allure.step('title'):
                allure.attach('title: {title}'.format(title=self.title), 'title')

        # 请求头参数，可不存在
        if "headers" in self.params['testcase'][index]['request'].keys():
            self.headers = self.params['testcase'][index]['request']['headers']
            with allure.step('headers'):
                allure.attach('headers: {headers}'.format(headers=self.headers), 'headers')

        # 请求url，必须存在
        if self.params['testcase'][index]['request']['url']:
            url = self.params['testcase'][index]['request']['url']
            if url[:1] is "/":
                self.url = ReadConfig().get_url + url
            else:
                self.url = url
            with allure.step('url'):
                allure.attach('url: {url}'.format(url=self.url), 'url')
        else:
            pytest.xfail(reason="name:{name}; title:{title};请加入请求地址url参数"
                         .format(name=self.name, title=self.title))

        # 请求方法，不可为空
        if self.params['testcase'][index]['request']['method']:
            self.method = self.params['testcase'][index]['request']['method']
            with allure.step('method'):
                allure.attach('method: {method}'.format(method=self.method), 'method')
        else:
            pytest.xfail(reason="name:{name}; title:{title};请加入请求方法method参数"
                         .format(name=self.name, title=self.title))

        # 请求body,可不存在
        if "body" in self.params['testcase'][index]['request'].keys():
            self.body = self.params['testcase'][index]['request']['body']
            with allure.step('body'):
                allure.attach('body: {body}'.format(body=self.body), "body")

        # 参数关联,可不存在
        if "link" in self.params['testcase'][index].keys():
            for key, value in self.params['testcase'][index]['link'].items():
                alias = key
                relation = self.params['testcase'][index]['link'][key]['relation']
                data = self.params['testcase'][index]['link'][key]['data']
                if relation == 'url':
                    # 替换url,再url中查找$alias$，用data下面的值替换
                    url_value = Link().replace_link(self.url, alias, data)
                    if url_value:
                        self.url = url_value
                elif relation == 'body':
                    body_value = Link().replace_link(self.body, alias, data)
                    if body_value:
                        self.body = body_value
                else:
                    pass

        # 请求中存在图片,可不存在
        if "image" in self.params['testcase'][index]['request'].keys():
            self.image = self.params['testcase'][index]['request']['image']

        # 请求中存在文件,可不存在
        if "file" in self.params['testcase'][index]['request'].keys():
            self.file = self.params['testcase'][index]['request']['file']

        # 预期结果,可不存在
        if 'check' in self.params['testcase'][index].keys():
            self.check = self.params['testcase'][index]['check']
        Logger().logs_file().debug("name:{name}; title:{title}".format(name=self.name, title=self.title))

        MemoryCase().add_memory_case_value(memory_case_key=index, headers=self.headers,
                                           body=self.body, url=self.url)

        YamlRequest(index=index, url=self.url, method=self.method, headers=self.headers,
                    body=self.body, image=self.image, file=self.file, check=self.check).yaml_request()
