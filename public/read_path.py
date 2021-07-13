
import os

BASE_PATH = os.path.abspath(os.path.dirname(os.getcwd()))
# # 添加为全局变量
# sys.path.append(BASE_PATH)

# config模块
# config.ini文件路径
CONFIGINI_PATH = BASE_PATH + os.path.sep + "config" + os.path.sep + "config.ini"
# email文件路径
EMAIL_PATH = BASE_PATH + os.path.sep + "config" + os.path.sep + "email.py"


# public模块
