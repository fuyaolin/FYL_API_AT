# -*- coding: utf-8 -*-
import paramiko


class SSHConfig(object):
    def __init__(self):
        self.ssh_content = {
            'host': '',
            'port': 80,
            'user': 'root',
            'passwd': ''
        }
        self.ssh = paramiko.SSHClient()

    def __enter__(self):
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            self.ssh.connect(self.ssh_content['host'], self.ssh_content['port'],
                             self.ssh_content['user'], self.ssh_content['passwd'])
        except Exception as e:
            print('conn failed', e)
        return self

    def run_command(self, cmd):
        try:
            stdin, stdout, stderr = self.ssh.exec_command(cmd)
            result = stdout.read().decode('utf-8').strip('\n')
            return result
        except Exception as e:
            print(f'run command: {cmd} failed', e)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.ssh.close()
