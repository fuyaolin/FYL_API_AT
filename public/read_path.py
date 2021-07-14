"""
    存储路径
"""
import os
import sys


BASE_PATH = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
# # 添加为全局变量
sys.path.append(BASE_PATH)

# config模块
# config.ini文件路径
CONFIG_INI_PATH = BASE_PATH + os.path.sep + "config" + os.path.sep + "config.ini"
# email文件路径
EMAIL_PATH = BASE_PATH + os.path.sep + "config" + os.path.sep + "email.py"


# public模块

# testcase_yaml模块
TESTCASE_YAML_PATH_test_01 = BASE_PATH + os.path.sep + "testcase_yaml" + os.path.sep + "test_01.yaml"