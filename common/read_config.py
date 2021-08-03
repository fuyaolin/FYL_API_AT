"""
    读取config配置内容
"""
# -*- coding: utf-8 -*-
from configparser import ConfigParser
from common.read_path import CONFIG_INI_PATH


class ReadConfig(object):
    def __init__(self):
        # 读取config.ini配置文件
        self.config = ConfigParser()
        self.config.read(CONFIG_INI_PATH, encoding='UTF-8')

    @property
    def get_url(self):
        get_url = self.config.get("link", "url")
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

    @property
    def get_email_sender(self):
        get_email_sender = self.config.get("email", "sender")
        return get_email_sender

    @property
    def get_email_sender_username(self):
        get_email_sender_username = self.config.get("email", "sender_username")
        return get_email_sender_username

    @property
    def get_email_sender_password(self):
        get_email_sender_password = self.config.get("email", "sender_password")
        return get_email_sender_password

    @property
    def get_email_receiver(self):
        get_email_receiver = self.config.get("email", "receiver")
        return get_email_receiver

    @property
    def get_email_CC(self):
        get_email_CC = self.config.get("email", "CC")
        return get_email_CC

    @property
    def get_smtp_server(self):
        get_smtp_server = self.config.get("email", "smtp_server")
        return get_smtp_server

    @property
    def get_smtp_port(self):
        get_smtp_port = self.config.get("email", "smtp_port")
        return get_smtp_port

