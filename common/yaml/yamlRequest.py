"""
    接口请求
"""
import requests
from assertfun.assertfunction import AssertResult


class YamlRequest(object):
    def __init__(self, method, url, headers, json_body, check):
        self.method = method
        self.url = url
        self.headers = headers
        self.json_body = json_body
        self.check = check

    def yaml_request(self):
        if self.method == 'get' or 'GET':
            self.yaml_get()
        elif self.method == 'post' or 'POST':
            self.yaml_post()
        elif self.method == 'put' or 'PUT':
            self.yaml_put()
        elif self.method == 'delete' or 'DELETE':
            self.yaml_delete()
        else:
            return "请输入正确的请求"

    def yaml_get(self):
        res = requests.get(headers=self.headers, url=self.url, data=self.json_body)
        self.res(res)

    def yaml_post(self):
        res = requests.post(headers=self.headers, url=self.url, data=self.json_body)
        self.res(res)

    def yaml_put(self):
        res = requests.put(headers=self.headers, url=self.url, data=self.json_body)
        self.res(res)

    def yaml_delete(self):
        res = requests.delete(headers=self.headers, url=self.url, data=self.json_body)
        self.res(res)

    def res(self, res):
        value = res.text
        code = res.status_code
        if self.check is None:
            pass
        else:
            AssertResult(check=self.check, value=value, code=code).expected()





