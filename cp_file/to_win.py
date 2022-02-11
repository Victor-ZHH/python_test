'''
使用subprocess模块执行scp命令
'''

import subprocess

workdir = "d:\\"
win_ip = "" # 登录Windowsip，用户名，密码
win_us = ""
win_pwd = ""
src_file_path = "" # 需要负责的文件的绝对路径

call_sh = [
    os.path.join(os.path.dirname(__file__), 'scp_win.sh'),
    win_ip, win_us, win_pwd,
    src_file_path,
    workdir]

subprocess.call(call_sh)


