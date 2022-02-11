# python 使用 find 命令搜索目标文件

import subprocess

def find(find_dir, filename):
    find_shell = f'find {find_dir} -name {filename} | grep -v target | sort -r'
    response = subprocess.run(
        find_shell, shell=True, capture_output=True, text=True)
    pom_paths = []
    if response.returncode == 0:
        res = response.stdout
        pom_paths = res.strip().split("\n")
    else:
        print(response.stderr)
    return pom_paths
