#!/usr/bin/env python
# -*- coding: utf-8 -*-

#==============#
#= cmdSsh =#
#==============#

import os
import paramiko
import socket
import sys

#configs
password = 'no_auth'
user = 'root'
port = 22
host = '192.168.101.1'


def connectSSH(host, port, user, password):
    ssh_client = None
    t = None
    try:
        ssh_client = paramiko.SSHClient()
        sock = socket.socket()
        sock.connect((host, port))
        t = paramiko.Transport(sock)
        t.connect()
        if password == 'no_auth':
            t.auth_none(user)
        else:
            t.auth_password(user, password)
        ssh_client._transport = t
    except:
        print 'EXCEPTION DURING CONNECTING SSH'
        print sys.exc_info()[0]
    if t!=None and t.is_active():
        return ssh_client


def sendCommandSSH(ssh_client, command):
    chan = ssh_client.get_transport().open_session()
    response = ''
    response_error = ''
    exit_code = -111
    commandToExecute = command.strip() + '\n'
    chan.exec_command(commandToExecute)
    while True:
        if chan.recv_ready():
            response += chan.recv(4096)
        if chan.recv_stderr_ready():
            response_error += chan.recv_stderr(4096)
        if chan.exit_status_ready():
            exit_code = chan.recv_exit_status()
            break
    return_value = (str(response) + str(response_error) + str(exit_code)).split('\n')
    return return_value


def closeSSH(ssh_client):
    ssh_client.close()


def Menu():
    os.system('cls')
    print """
    =================
    =  cmdSsh       =
    =================
    1 - sw rev
    2 - unit
    3 - 17
    4 - zombie
    5 - hwid
    6 - Exit
    =================
    """
    choice = raw_input("Enter a choice and press enter:  ")
    return choice

#TAKE CHOICE AND LAUNCH MODULE



choice = ""

while choice != "6":
    choice = Menu()
    if choice == "1":
        os.system('cls')
        rfm = connectSSH(host, port, user, password)
        cmd = 'cat /etc/issue'
        out = sendCommandSSH(rfm, cmd)
        print out
        closeSSH(rfm)
        raw_input("Press enter to continue:  ")
    elif choice == "2":
        os.system('cls')
        rfm = connectSSH(host, port, user, password)
        cmd = 'ls /mnt/factory/configs/unit'
        out = sendCommandSSH(rfm, cmd)
        print out
        closeSSH(rfm)
        raw_input("Press enter to continue:  ")
    elif choice == "3":
        os.system('cls')
        rfm = connectSSH(host, port, user, password)
        cmd = 'ls /mnt/factory/configs/17/REV_0'
        out = sendCommandSSH(rfm, cmd)
        print out
        closeSSH(rfm)
        raw_input("Press enter to continue:  ")
    elif choice == "4":
        os.system('cls')
        rfm = connectSSH(host, port, user, password)
        cmd = "ps | grep 'Z'"
        out = sendCommandSSH(rfm, cmd)
        print out
        closeSSH(rfm)
        raw_input("Press enter to continue:  ")
    elif choice == "5":
        os.system('cls')
        rfm = connectSSH(host, port, user, password)
        cmd = 'cat /mnt/factory/configs/unit/hwid.txt'
        out = sendCommandSSH(rfm, cmd)
        print out
        closeSSH(rfm)
        raw_input("Press enter to continue:  ")
