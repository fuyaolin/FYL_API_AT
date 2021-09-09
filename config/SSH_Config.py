# -*- coding: utf-8 -*-
import paramiko


class SSHConfig(object):
    def __init__(self):
        ssh_content = {
            'host': '',
            'port': 80,
            'user': 'root',
            'passwd': ''
        }
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(ssh_content['host'], ssh_content['port'], ssh_content['user'], ssh_content['passwd'])

    def execmd(self, cmd):
        stdin, stdout, stderr = self.ssh.exec_command(cmd)
        result = stdout.read().decode('utf-8').strip('\n')
        return result

    def sshclose(self):
        self.ssh.close()
