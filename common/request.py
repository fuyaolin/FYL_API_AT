"""
    接口请求
"""
import requests
import pytest
import json
import os
from common.log import Logger
from assertfun.assertfunction import AssertResult
from common.read_path import IMAGE_PATH


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
        Logger().logs_file().debug("method:"+str(method)+",url:"+str(url)+",body:"+str(body))

    def files_type(self, file_name, file_type):
        # 查找文件/图片路径
        file_path = IMAGE_PATH + os.sep + file_name
        if os.path.exists(file_path) is False:
            pytest.xfail(str(file_path) + "路径找不到")
        # 判断文件/图片类型
        req_type = "text/plain"
        types = self.file_name.split(".")[-1]
        if file_type == "image":
            if types in ['jpg']:
                req_type = "image/jpeg"
            elif types in ['png']:
                req_type = "image/png"
            else:
                req_type = None
        elif file_type == "file":
            if types in ['html']:
                req_type = "text/html"
            elif types in ['zip']:
                req_type = "application/zip"
            elif types in ['json']:
                req_type = "application/json"
            elif types in ['xml']:
                req_type = "text/xml"
            else:
                req_type = "text/plain"
        else:
            raise Exception("文件类型错误")
        with open(file_path, 'rb') as f:
            file = {"multipartFile": (file_path, f.read(), req_type)}
        return file

    def yaml_request(self):
        if self.method == ('get' or 'GET'):
            self.yaml_get()
        elif self.method == ('post' or 'POST') and (self.file_name or self.image_name) is None:
            self.yaml_post()
        elif self.method == ('post' or 'POST') and (self.file_name or self.image_name) is not None:
            self.yaml_files_post()
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

    def yaml_files_post(self):
        # 只上传图片
        files = None
        if self.image_name is not None and self.file_name is None:
            files = self.files_type(self.image_name, "image")
        # 只上传文件
        elif self.file_name is not None and self.image_name is None:
            files = self.files_type(self.image_name, "file")
        # 均上传
        else:
            pytest.skip("目前未实现")
        res = requests.post(headers=self.headers, url=self.url, data=json.dumps(self.body), files=files, timeout=30)
        self.res(res)

    def yaml_put(self):
        res = requests.put(headers=self.headers, url=self.url, data=json.dumps(self.body), timeout=30)
        self.res(res)

    def yaml_delete(self):
        res = requests.delete(headers=self.headers, url=self.url, data=json.dumps(self.body), timeout=30)
        self.res(res)

    def yaml_patch(self):
        res = requests.patch(headers=self.headers, url=self.url, data=json.dumps(self.body), timeout=30)
        self.res(res)

    def yaml_options(self):
        res = requests.options(headers=self.headers, url=self.url, data=json.dumps(self.body), timeout=30)
        self.res(res)

    def yaml_head(self):
        res = requests.head(headers=self.headers, url=self.url, data=json.dumps(self.body), timeout=30)
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
