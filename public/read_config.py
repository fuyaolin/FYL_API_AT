"""
    读取config配置内容
"""
# -*- coding: utf-8 -*-
from configparser import ConfigParser
from public.read_path import CONFIGINI_PATH

class ReadConfig(object):
    def __init__(self):
        # 读取config.ini配置文件
        self.config = ConfigParser()
        self.config.read(CONFIGINI_PATH, encoding='UTF-8')

    @property
    def get_url(self):
        get_url = self.config.get("link","url")
        return get_url

    @property
    def get_ip(self):
        get_ip = self.config.get("link", "ip")
        return get_ip

    @property
    def get_port(self):
        get_port = self.config.get("link", "port")
        return get_port