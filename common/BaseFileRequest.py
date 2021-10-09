"""
    请求参数带文件/图片上传
"""
import os
import pytest
from common.ReadPath import RES_IMAGE_PATH, RES_FILE_PATH


class RequestFile(object):
    def __init__(self):
        pass

    def files_up(self, file_name):
        if file_name is not None:
            # 查找图片路径
            file_path = RES_FILE_PATH + os.sep + file_name
            if os.path.exists(file_path) is False:
                pytest.xfail(str(file_path) + "路径找不到")
            else:
                # 判断文件类型
                types = file_name.split(".")[-1]
                if types in ['report']:
                    req_type = "text/report"
                elif types in ['zip']:
                    req_type = "application/zip"
                elif types in ['json']:
                    req_type = "application/json"
                elif types in ['xml']:
                    req_type = "text/xml"
                else:
                    req_type = "text/plain"
                with open(file_path, 'rb') as f:
                    file = {"multipartFile": (file_path, f.read(), req_type)}
                return file
        else:
            return None

    def image_up(self, image_name):
        if image_name is not None:
            image_path = RES_IMAGE_PATH + os.sep + image_name
            if os.path.exists(image_path) is False:
                pytest.xfail(str(image_path) + "路径找不到")
            else:
                types = image_path.split(".")[-1]
                if types in ['jpg']:
                    req_type = "image/jpeg"
                elif types in ['png']:
                    req_type = "image/png"
                else:
                    req_type = None
                with open(image_path, 'rb') as f:
                    file = {"multipartFile": (image_path, f.read(), req_type)}
                return file
        else:
            return None
