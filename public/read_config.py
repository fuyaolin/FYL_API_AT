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
        get_port = int(get_port)
        return int(get_port)

    @property
    def get_mysql_port(self):
        get_mysql_port = self.config.get("mysql_con", "mysql_port")
        return int(get_mysql_port)

    @property
    def get_mysql_database(self):
        get_mysql_database = self.config.get("mysql_con", "mysql_database")
        return get_mysql_database

    @property
    def get_mysql_user(self):
        get_mysql_user = self.config.get("mysql_con", "mysql_user")
        return get_mysql_user

    @property
    def get_mysql_passwd(self):
        get_mysql_passwd = self.config.get("mysql_con", "mysql_passwd")
        return get_mysql_passwd

    @property
    def get_mysql_charset(self):
        get_mysql_charset = self.config.get("mysql_con", "mysql_charset")
        return get_mysql_charset
