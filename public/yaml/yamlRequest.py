"""
    接口请求
"""
import requests


class YamlRequest(object):
    def __init__(self, method, url, headers, json_body, check):
        self.method = method
        self.url = url
        self.headers = headers
        self.json_body = json_body
        self.check = check

    def yaml_request(self):
        yaml_request = "yaml_" + self.method
        # YamlRequest.yaml_request

    def yaml_get(self):
        requests.get(headers=self.headers, url=self.url, body=self.json_body)

    def yaml_post(self):
        requests.post(headers=self.headers, url=self.url, body=self.json_body)

    def yaml_put(self):
        requests.put(headers=self.headers, url=self.url, body=self.json_body)

    def yaml_delete(self):
        requests.delete(headers=self.headers, url=self.url, body=self.json_body)