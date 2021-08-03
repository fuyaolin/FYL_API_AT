"""
    固定存储路径
"""
import os
import sys


BASE_PATH = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
# # 添加为全局变量
sys.path.append(BASE_PATH)

# config模块
# config下config.ini文件路
CONFIG_INI_PATH = BASE_PATH + os.path.sep + "config" + os.path.sep + "config.ini"
# config下email文件路径
EMAIL_PATH = BASE_PATH + os.path.sep + "config" + os.path.sep + "sendemail.py"

# testcase_yaml模块
# testcase_yaml文件夹路径
TESTCASE_YAML_PATH = BASE_PATH + os.path.sep + "testcase_yaml"

# 报告路径
REPORT_PATH = 1