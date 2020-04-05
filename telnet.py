# This program checks if a port is open in a specific host
# Author : Soutrik Chatterjee


import telnetlib
import socket
import os
import subprocess

new_socket = socket.socket()

host = input("Enter IP address of the machine ")
port = int(input("Enter the port to check "))

try :
	s = new_socket.connect((host, port))
	print("Connection Successful")
except InterruptedError :
	print("Connection Interrupted")
except TimeoutError :
	print("Connection Timed out")
except ConnectionRefusedError :
	print("Connection refused by remote host")
finally :
	if new_socket.timeout :
		print("Connection Failure")

w = input("Press enter to exit") 