#!/usr/bin/expect
set timeout 30
set host [lindex $argv 0]
set username [lindex $argv 1]
set password [lindex $argv 2]
set src_file [lindex $argv 3]
set dir [lindex $argv 4]

spawn scp ${src_file} ${username}@${host}:${dir}
expect {
        "yes/no" {send "yes\r"; exp_continue}
        "password:" {send "${password}\r"; exp_continue}
        eof
    }
