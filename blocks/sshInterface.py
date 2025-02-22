#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import paramiko
import socket
import sys

#configs
password = 'no_auth'
user = 'root'
port = 22
host = '192.168.101.1'
command = 'ps'

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


connection = connectSSH(host, port, user, password)
out = sendCommandSSH(connection, command)
print out
closeSSH(connection)
raw_input("Press enter to continue:  ")