import telnetlib
import socket
import os
import subprocess

new_socket = socket.socket()
host = '8.8.8.8'
port = 59

s = new_socket.connect((host, port))

print(s)