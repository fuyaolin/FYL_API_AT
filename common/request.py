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
        self.file = image
        self.image = file
        self.check = check
        if (self.method or self.url) is None:
            Logger().logs_file().info("method is None or url is None")
            pytest.xfail(reason="method is None or url is None")
        Logger().logs_file().debug("method:"+str(method)+",url:"+str(url)+",body:"+str(body))

    def yaml_request(self):
        if self.method == ('get' or 'GET'):
            self.yaml_get()
        elif self.method == ('post' or 'POST') and (self.file or self.image) is None:
            self.yaml_post()
        elif self.method == ('post' or 'POST') and (self.file or self.image) is not None:
            self.yaml_files_post()
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

    # 未完成，待修改
    def yaml_files_post(self):
        # 只上传图片
        if self.image is not None and self.file is None:
            image_name = IMAGE_PATH + os.sep + self.image
            if os.path.exists(image_name) is False:
                pytest.xfail(str(image_name) + "路径找不到")
            # 使用with打开图片后自动关闭，直接用open后面会报未关闭图片错误
            with open(image_name, 'rb') as f:
                # self.body['multipartFile'] = (file_name, f.read(), "image/jpeg")
                file = {"multipartFile": (image_name, f.read(), "image/jpeg")}  # "image/jpeg"照片格式
        # 只上传文件
        elif self.file is not None and self.image is None:
            file_name = IMAGE_PATH + os.sep + self.file
            if os.path.exists(file_name) is False:
                pytest.xfail(str(file_name) + "路径找不到")
            if self.file.split(".")[-1] == "zip":
                with open(file_name, 'rb')as f:
                    # "application/zip"zip格式
                    file = {"multipartFile": (file_name, f.read(), "application/zip")}
            else:
                with open(file_name, 'rb')as f:
                    file = {"multipartFile": (file_name, f.read())}
        # 均上传
        else:
            pass
        res = requests.post(headers=self.headers, url=self.url, data=json.dumps(self.body), files=file, timeout=30)
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
