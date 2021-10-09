"""
    接口请求
"""
import requests
import pytest
import json
import allure
from common.UpdateLog import Logger
from assertfun.AssertFunction import AssertResult
from common.BaseFileRequest import RequestFile
from common.MemoryCase import MemoryCase


class YamlRequest(object):
    def __init__(self, index, method, url, headers, body, image, file, check):
        self.index = index
        self.method = method
        self.url = url
        self.headers = headers
        self.body = body
        self.image_name = image
        self.file_name = file
        self.check = check
        if (self.method or self.url) is None:
            Logger().logs_file().info("method is None or url is None")
            pytest.xfail(reason="method is None or url is None")
        Logger().logs_file().debug("method:{method},url:{url},body:{body}".format(method=method, url=url, body=body))

    def yaml_request(self):
        if self.method == ('get' or 'GET'):
            self.yaml_get()
        elif self.method == ('post' or 'POST'):
            if self.file_name is not None:
                self.yaml_files_post()
            elif self.image_name is not None:
                self.yaml_image_post()
            else:
                self.yaml_post()
        elif self.method == ('put' or 'PUT'):
            self.yaml_put()
        elif self.method == ('delete' or 'DELETE'):
            self.yaml_delete()
        elif self.method == ('patch' or 'PATCH'):
            self.yaml_patch()
        elif self.method == ('options' or 'OPTIONS'):
            self.yaml_options()
        elif self.method == ('head' or 'HEAD'):
            self.yaml_head()
        else:
            pytest.xfail(reason="请输入正确的请求")

    def yaml_get(self):
        try:
            res = requests.get(headers=self.headers, url=self.url, data=json.dumps(self.body), timeout=30)
            self.res(res)
        except requests.exceptions.RequestException:
            exception = requests.exceptions.RequestException
            pytest.xfail(reason=str(exception))

    def yaml_post(self):
        try:
            res = requests.post(headers=self.headers, url=self.url, data=json.dumps(self.body), timeout=30)
            self.res(res)
        except requests.exceptions.RequestException:
            exception = requests.exceptions.RequestException
            pytest.xfail(reason=str(exception))

    def yaml_put(self):
        try:
            res = requests.put(headers=self.headers, url=self.url, data=json.dumps(self.body), timeout=30)
            self.res(res)
        except requests.exceptions.RequestException:
            exception = requests.exceptions.RequestException
            pytest.xfail(reason=str(exception))

    def yaml_delete(self):
        try:
            res = requests.delete(headers=self.headers, url=self.url, data=json.dumps(self.body), timeout=30)
            self.res(res)
        except requests.exceptions.RequestException:
            exception = requests.exceptions.RequestException
            pytest.xfail(reason=str(exception))

    def yaml_patch(self):
        try:
            res = requests.patch(headers=self.headers, url=self.url, data=json.dumps(self.body), timeout=30)
            self.res(res)
        except requests.exceptions.RequestException:
            exception = requests.exceptions.RequestException
            pytest.xfail(reason=str(exception))

    def yaml_options(self):
        try:
            res = requests.options(headers=self.headers, url=self.url, data=json.dumps(self.body), timeout=30)
            self.res(res)
        except requests.exceptions.RequestException:
            exception = requests.exceptions.RequestException
            pytest.xfail(reason=str(exception))

    def yaml_head(self):
        try:
            res = requests.head(headers=self.headers, url=self.url, data=json.dumps(self.body), timeout=30)
            self.res(res)
        except requests.exceptions.RequestException:
            exception = requests.exceptions.RequestException
            pytest.xfail(reason=str(exception))

    def yaml_files_post(self):
        try:
            files = RequestFile().files_up(self.file_name)
            res = requests.post(headers=self.headers, url=self.url, data=json.dumps(self.body), files=files, timeout=30)
            self.res(res)
        except requests.exceptions.RequestException:
            exception = requests.exceptions.RequestException
            pytest.xfail(reason=str(exception))

    def yaml_image_post(self):
        try:
            files = RequestFile().image_up(self.image_name)
            res = requests.post(headers=self.headers, url=self.url, data=json.dumps(self.body), files=files, timeout=30)
            self.res(res)
        except requests.exceptions.RequestException:
            exception = requests.exceptions.RequestException
            pytest.xfail(reason=str(exception))

    def res(self, res):
        value = res.text
        code = res.status_code
        with allure.step("response"):
            allure.attach("response: {response}".format(response=value), "response")
        MemoryCase().add_memory_case(memory_case_key=self.index, response=value)
        Logger().logs_file().debug("status：{status};response:{value}".format(status=code, value=value))
        if self.check is None:
            # 没有检查点，永远成立
            actual_value = "status：{status};response:{value}".format(status=code, value=value)
            with allure.step("check"):
                allure.attach("预期结果：{expect_value}；实际结果：{actual_value}"
                              .format(expect_value="未设置", actual_value=actual_value), "check")
            Logger().logs_file().debug("没有检查点，永远成立")
            assert True
        else:
            AssertResult(check=self.check, value=value, code=code).expected()
