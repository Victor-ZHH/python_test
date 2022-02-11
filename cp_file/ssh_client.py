from paramiko import SSHClient


class BufSSHClient(SSHClient):

    def run(self, command, callback):
        trans = self.get_transport()
        chan = trans.open_session()
        chan.get_pty(width=200)
        chan.exec_command(command)
        stdout = chan.makefile("r", -1)
        stderr = chan.makefile_stderr("r", -1)
        while not stdout.channel.exit_status_ready():
            result = stdout.readline()
            callback(result.strip())

            # 由于在退出时，stdout还是会有一次输出，因此需要单独处理，处理完之后，就可以跳出了
            if stdout.channel.exit_status_ready():
                last_stdout = stdout.readlines()
                for res in last_stdout:
                    callback(res.strip())
                break

        return stdout, stderr