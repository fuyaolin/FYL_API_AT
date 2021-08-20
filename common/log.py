import logging
import logging.handlers
import os
from datetime import datetime
from common.read_path import LOGS_PATH

LOGS_FILE_PATH = LOGS_PATH + os.path.sep + datetime.now().strftime("%Y-%m-%d") + "AT_logs.log"
NAME = "root"


class Logger(object):
    def __init__(self):
        # 创建一个logger
        self.logger = logging.getLogger(NAME)
        self.logger.setLevel(level=logging.DEBUG)
        # 日志格式
        self.matter = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

    def logs_file(self):
        # 创建一个handler，用于写入日志文件
        handle = logging.handlers.TimedRotatingFileHandler(LOGS_FILE_PATH, when='D', encoding='UTF-8')
        handle.setLevel(level=logging.DEBUG)
        # 生成并设置日志格式
        handle.setFormatter(logging.Formatter(self.matter))
        self.logger.addHandler(handle)
        return self.logger

    def logs_cmd(self):
        cmd_handle = logging.StreamHandler()
        cmd_handle.setLevel(level=logging.DEBUG)
        cmd_handle.setFormatter(logging.Formatter(self.matter))
        self.logger.addHandler(cmd_handle)
        return self.logger

# if __name__ == '__main__':
    # Logger().logs_file().debug("aaa")
    # Logger().logs_cmd().debug("aaa")
