"""
    固定存储路径
"""
import os
import sys


BASE_PATH = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
# 添加为全局变量
sys.path.append(BASE_PATH)

# 测试用例统用模板
TESTCASE_PY_TEMPLATE_PATH = BASE_PATH + os.sep + "common" + os.sep + "template" + os.sep + "testcase_py_template.txt"
TESTCASE_YAML_TEMPLATE_PATH = BASE_PATH + os.sep + "common" + os.sep + "template" + os.sep +"testcase_yaml_template.yaml"

# config模块
# config下config.ini文件路
CONFIG_INI_PATH = BASE_PATH + os.sep + "config" + os.sep + "config.ini"
# config下email文件路径
EMAIL_PATH = BASE_PATH + os.path.sep + "config" + os.path.sep + "Send_Email.py"

# 前置文件路径
SETUP_PATH = BASE_PATH + os.path.sep + "public" + os.path.sep + "setup"
# 后置文件路径
TEARDOWN_PATH = BASE_PATH + os.path.sep + "public" + os.path.sep + "teardown"

# log日志报告路径
LOGS_PATH = BASE_PATH + os.path.sep + "logs"

# excel表格路径
EXCEL_PATH = BASE_PATH + os.path.sep + "excel"

# 图片文件路径
RES_IMAGE_PATH = BASE_PATH + os.path.sep + "up_or_down" + os.path.sep + "image"
RES_FILE_PATH = BASE_PATH + os.path.sep + "up_or_down" + os.path.sep + "file"

# testcase_py文件夹路径
TESTCASE_PY_PATH = BASE_PATH + os.path.sep + "testcase_py"
TESTCASE_PY_NAME_PATH = os.path.realpath(sys.argv[0])

# testcase_yaml模块
# testcase_yaml文件夹路径
TESTCASE_YAML_PATH = BASE_PATH + os.path.sep + "testcase_yaml"
TESTCASE_YAML_NAME_PATH = os.path.realpath(sys.argv[0]).replace("testcase_py", "testcase_yaml").replace(".py", ".yaml")
# allure报告路径
REPORT_REPORT_PATH = BASE_PATH + os.path.sep + "report_allure" + os.path.sep + "html"
REPORT_RESULT_PATH = BASE_PATH + os.path.sep + "report_allure" + os.path.sep + "result"
# html报告路径
HTML_REPORT_PATH = BASE_PATH + os.path.sep + "report_html"