import telnetlib
import socket
import os
import subprocess

new_socket = socket.socket()
host = '192.168.0.11'
port = 81

try :
	s = new_socket.connect((host, port))
except InterruptedError :
	print("Connection Interrupted")
except TimeoutError :
	print("Connection Timed out")
finally :
	if new_socket.timeout :
		print("Connection Failure")
