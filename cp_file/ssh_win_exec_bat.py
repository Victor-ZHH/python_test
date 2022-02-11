# 连接windows执行bat脚本
from paramiko import AutoAddPolicy
from .ssh_client import SSHClient


class ExecBat:
    def __init__(self, ip, username, pwd, file_path):
        self._log = []
        self.win_ip = ip # 登录Windowsip，用户名，密码
        self.win_us = username
        self.win_pwd = pwd
        self.windows_bat_path = file_path # bat 文件的绝对路径

    def __str__(self):
        print("".join(self._log))

    def win_stdout(self, stdout):  
        self._log.append(stdout)
    
    def exec(self):
        ssh = BufSSHClient()
        ssh.set_missing_host_key_policy(AutoAddPolicy())
        ssh.connect(
            hostname=self.win_ip,
            port=22,
            username=self.win_us,
            password=self.win_pwd
        )

        stdout, stderr = ssh.run(
            self.windows_bat_path, self.win_stdout)

        if stdout.channel.recv_exit_status() != 0:
            self.win_stdout(stderr.read())
