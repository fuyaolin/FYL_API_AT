"""
    接口请求
"""
import requests
import pytest
import json
from common.log import Logger
from assertfun.assertfunction import AssertResult


class YamlRequest(object):
    def __init__(self, index, method, url, headers, body, check):
        self.index = index
        self.method = method
        self.url = url
        self.headers = headers
        self.body = body
        self.check = check
        if (self.method or self.url) is None:
            Logger().logs_file().info("method is None or url is None")
            pytest.xfail(reason="method is None or url is None")
        Logger().logs_file().debug("method:"+str(method)+",url:"+str(url)+",body:"+str(body))

    def yaml_request(self):
        if self.method == ('get' or 'GET'):
            self.yaml_get()
        elif self.method == ('post' or 'POST'):
            self.yaml_post()
        elif self.method == ('put' or 'PUT'):
            self.yaml_put()
        elif self.method == ('delete' or 'DELETE'):
            self.yaml_delete()
        else:
            pytest.xfail(reason="请输入正确的请求")

    def yaml_get(self):
        # try:
        #     res = requests.get(headers=self.headers, url=self.url, data=json.dumps(self.body), timeout=30)
        #     self.res(res)
        # except requests.exceptions.ConnectTimeout:
        #     pytest.xfail("请求超时")
        res = requests.get(headers=self.headers, url=self.url, data=json.dumps(self.body), timeout=30)
        self.res(res)

    def yaml_post(self):
        res = requests.post(headers=self.headers, url=self.url, data=json.dumps(self.body), timeout=30)
        self.res(res)

    def yaml_put(self):
        res = requests.put(headers=self.headers, url=self.url, data=json.dumps(self.body), timeout=30)
        self.res(res)

    def yaml_delete(self):
        res = requests.delete(headers=self.headers, url=self.url, data=json.dumps(self.body), timeout=30)
        self.res(res)

    def res(self, res):
        value = res.text
        code = res.status_code
        Logger().logs_file().debug("实际返回结果为：status："+str(code)+",value:"+str(value))
        if self.check is None:
            # 没有检查点，永远成立
            Logger().logs_file().debug("没有检查点，永远成立")
            assert True
        else:
            AssertResult(check=self.check, value=value, code=code).expected()

