# -*- coding: utf-8 -*-
import os
from ftplib import FTP
from common.Read_Config import ReadConfig


class FtpConnect(object):
    def __init__(self):
        ftp_content = {
            'host': ReadConfig().get_ftp_host,
            # 'host': '',
            # 'port': ReadConfig().get_ftp_port,
            'port': 21,
            'user': '',
            'passwd': ''
        }
        try:
            self.ftp = FTP()
            self.ftp.connect(host=ftp_content['host'], port=ftp_content['port'])
            self.ftp.login(user=ftp_content['user'], passwd=ftp_content['passwd'])
        except Exception:
            raise Exception("登陆FTP失败，请检查")
        self.ftp.encoding = 'utf-8'
        # False:主动模式   True：被动模式
        # 默认是主动模式
        self.ftp.set_pasv(False)

    # 上传文件夹
    def up_ftp_dir(self, local_dir_path, ftp_file_path):
        """
        :param local_dir_path: 本地文件夹
        :param ftp_file_path: 上传后保存文件名称组
        :return:
        """
        if not os.path.isdir(local_dir_path):
            print("文件夹路径不存在： %s" % local_dir_path)
            return
        try:
            # 切换至远程目录
            self.ftp.cwd(ftp_file_path)
            ##################未完成
        except Exception as err:
            raise Exception("问价夹为 %s ,上传失败, 具体错误描述为：%s" % (local_dir_path, err))
        finally:
            self.down_ftp_file()

    # 上传单个文件
    def up_ftp_file(self, local_file_path, ftp_file_path):
        """
        :param local_file_path: 本地文件路径
        :param ftp_file_path: 上传后保存文件名称
        :return:
        """
        if not os.path.isfile(local_file_path):
            print("文件路径不存在： %s" % local_file_path)
            return
        try:
            buf_size = 1024
            fp = open(local_file_path, 'rb')
            # size = os.path.getsize(local_file_path)
            self.ftp.storbinary('STOR ' + ftp_file_path, fp, buf_size)
        except Exception as err:
            raise Exception("文件为 %s ,上传失败, 具体错误描述为：%s" % (local_file_path, err))
        finally:
            self.down_ftp_file()

    # 下载文件
    def down_ftp_file(self):
        pass

    def ftp_quit(self):
        # 关闭ftp 连接
        self.ftp.quit()