# -*- coding: utf-8 -*-
import os
from ftplib import FTP
from common.Read_Config import ReadConfig
from common.Log import Logger


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

    # 判断远程文件和本地文件大小是否一致
    def is_same_size(self, local_file, ftp_file):
        """
             local_file: 本地文件
             ftp_file: ftp文件
        """
        try:
            remote_file_size = self.ftp.size(ftp_file)
        except Exception as err:
            remote_file_size = -1
            Logger().logs_file().warning("%s 文件大小获取失败, % s" % (ftp_file, err))

        try:
            local_file_size = os.path.getsize(local_file)
        except Exception as err:
            local_file_size = -1
            Logger().logs_file().warning("%s 文件大小获取失败, % s" % (local_file, err))

        if remote_file_size == local_file_size:
            return 1
        else:
            return 0

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
            local_name_list = os.listdir(local_dir_path)
            for local_name in local_name_list:
                local_path = os.path.join(local_dir_path, local_name)
                if os.path.isdir(local_name):
                    try:
                        self.ftp.mkd(local_name)
                    except Exception as err:
                        Logger().logs_file().warning("%s 上传ftp新建目录失败，错误信息： %s" % (local_path, err))
                    self.up_ftp_dir(local_path, local_name)
                else:
                    self.up_ftp_file(local_path, '', local_name)
        except Exception as err:
            raise Exception("文件夹为 %s ,上传失败, 具体错误描述为：%s" % (local_dir_path, err))
        finally:
            self.ftp.cwd("..")
            # self.ftp_quit()

    # 上传单个文件
    def up_ftp_file(self, local_file_path, ftp_file_path, ftp_file_name):
        """
        :param local_file_path: 本地文件路径
        :param ftp_file_path: 上传的路径
        :param ftp_file_name: 上传后保存文件名称
        :return:
        """
        if not os.path.isfile(local_file_path):
            return "文件路径不存在： %s" % local_file_path

        if self.is_same_size(local_file_path.split('\\')[-1], ftp_file_name):
            return "%s 和 %s 文件名称相同" % (local_file_path, ftp_file_name)

        if ftp_file_path != '':
            try:
                self.ftp.cwd(ftp_file_path)
            except Exception as err:
                Logger().logs_file().warning("%s 跳转ftp目录失败，错误信息： %s" % (ftp_file_path, err))

        try:
            buf_size = 1024
            fp = open(local_file_path, 'rb')
            self.ftp.storbinary('STOR ' + ftp_file_name, fp, buf_size)
        except Exception as err:
            raise Exception("文件为 %s ,上传失败, 具体错误描述为：%s" % (local_file_path, err))
        finally:
            self.ftp.cwd("..")
        #     self.ftp_quit()

    # 下载文件
    def down_ftp_file(self, local_file_path, ftp_file_path):
        """
        :param local_file_path: 本地文件路径
        :param ftp_file_path: ftp文件路径
        :return:
        """

    def ftp_quit(self):
        # 关闭ftp 连接
        self.ftp.quit()
