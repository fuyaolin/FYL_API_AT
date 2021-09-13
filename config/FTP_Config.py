# -*- coding: utf-8 -*-
import os
from ftplib import FTP
import shutil
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
        self.buf_size = 1024
        self.file_list = []
        try:
            self.ftp = FTP()
            self.ftp.connect(host=ftp_content['host'], port=ftp_content['port'])
            self.ftp.login(user=ftp_content['user'], passwd=ftp_content['passwd'])
            Logger().logs_file().debug("登陆FTP成功")
        except Exception:
            Logger().logs_file().warning("登陆FTP失败，请检查")
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
        except:
            remote_file_size = -1

        try:
            local_file_size = os.path.getsize(local_file)
        except:
            local_file_size = -1

        if remote_file_size == local_file_size:
            return True
        else:
            return False

    # 上传单个文件
    def up_ftp_file(self, local_file_path, ftp_file_path):
        """
        :param local_file_path: 本地文件路径
        :param ftp_file_path: 上传的路径
        :return:
        """
        if not os.path.isfile(local_file_path):
            return "文件路径不存在： %s" % local_file_path

        if self.is_same_size(local_file_path, ftp_file_path):
            return "本地文件%s 和ftp上文件 %s 文件 大小名称 相同，因此不重新上传" % (local_file_path, ftp_file_path)

        try:
            fp = open(local_file_path, 'rb')
            self.ftp.storbinary('STOR %s ' % ftp_file_path, fp, self.buf_size)
            fp.close()
            Logger().logs_file().info("上传文件 %s 成功,ftp位置为： %s" % (local_file_path, ftp_file_path))
        except Exception as err:
            Logger().logs_file().warning("文件为 %s ,上传失败, 具体错误描述为：%s" % (local_file_path, err))
            raise Exception("文件为 %s ,上传失败, 具体错误描述为：%s" % (local_file_path, err))
        finally:
            self.ftp.cwd("..")
        #     self.ftp_quit()

    # 上传文件夹
    def up_ftp_dir(self, local_dir_path, ftp_dir_path):
        """
        :param local_dir_path: 本地文件夹
        :param ftp_dir_path: 上传后保存文件名称组
        :return:
        """
        if not os.path.isdir(local_dir_path):
            Logger().logs_file().warning("文件夹路径不存在： %s" % local_dir_path)
            return "文件夹路径不存在： %s" % local_dir_path

        # 切换至远程目录
        try:
            self.ftp.cwd(ftp_dir_path)
        except:
            self.ftp.cwd('..')
            self.ftp.mkd(ftp_dir_path)

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
                self.up_ftp_file(local_path, local_name)
        Logger().logs_file().info("上传文件夹 %s 成功,ftp位置为： %s" % (local_dir_path, ftp_dir_path))
        # self.ftp_quit()

    # 下载文件
    def down_ftp_file(self, local_path, ftp_path):
        """
        :param local_path: 本地文件路径
        :param ftp_path: 下载文件
        :return:
        """
        if os.path.exists(local_path):
            os.remove(local_path)

        try:
            fp = open(local_path, 'wb')
            self.ftp.retrbinary('RETR %s' % ftp_path, fp.write, self.buf_size)
            fp.close()
        except Exception as err:
            Logger().logs_file().warning("下载文件 %s 失败，具体错误描述为： %s" % ftp_path, err)
            return "下载文件 %s 失败，具体错误描述为： %s" % ftp_path, err

    # 下载文件夹
    def down_ftp_dir(self, local_dir_path, ftp_dir_path):
        """
        :param local_dir_path:
        :param ftp_dir_path:
        :return:
        """
        try:
            self.ftp.cwd(ftp_dir_path)
        except Exception as err:
            Logger().logs_file().warning("ftp跳转路径 %s 失败" % ftp_dir_path)
            return "ftp跳转路径 %s 失败, 具体错误描述为：" % ftp_dir_path, err

        if os.path.isdir(local_dir_path):
            shutil.rmtree(local_dir_path)
        os.makedirs(local_dir_path)

        # 方法回调
        self.file_list = []
        self.ftp.dir(self.get_file_list)

        remote_names = self.file_list
        for item in remote_names:
            file_type = item[0]
            file_name = item[1]
            local = os.path.join(local_dir_path, file_name)
            print(local, file_name)
            if file_type == 'd':
                self.down_ftp_dir(local, file_name)
            elif file_type == '-':
                self.down_ftp_dir(local, file_name)
            self.ftp.cwd("..")
        return True

    def get_file_list(self, line):
        """ 获取文件列表"""
        print(line)
        file_arr = self.get_file_name(line)
        # 去除  . 和  ..
        if file_arr[1] not in ['.', '..']:
            self.file_list.append(file_arr)

    @staticmethod
    def get_file_name(line):
        """ 获取文件名"""
        pos = line.rfind(':')
        while line[pos] != ' ':
            pos += 1
        while line[pos] == ' ':
            pos += 1
        file_arr = [line[0], line[pos:]]
        return file_arr

    def ftp_quit(self):
        # 关闭ftp 连接
        self.ftp.quit()
        Logger().logs_file().debug("关闭FTP连接")
