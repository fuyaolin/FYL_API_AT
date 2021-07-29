import requests


class YamlRequest(object):
    def __init__(self, url, headers, body, check):
        self.url = url
        self.headers = headers
        self.body = body
        self.check= check

    def yaml_get(self):
        requests.get(headers=self.headers, url=self.url, body=self.body)

    def yaml_post(self):
        requests.post(headers=self.headers, url=self.url, body=self.body)

    def yaml_put(self):
        requests.put(headers=self.headers, url=self.url, body=self.body)

    def yaml_delete(self):
        requests.delete(headers=self.headers, url=self.url, body=self.body)
