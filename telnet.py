# This program checks if a port is open in a specific host
# Author : Soutrik Chatterjee

import time
import socket

new_socket = socket.socket()

host = input("Enter IP address of the machine ")
port = int(input("Enter the port to check "))

start = time.perf_counter()

try :
	s = new_socket.connect((host, port))
	print("Connection Successful")
	print("Time taken to establish the connection = ", time.perf_counter() - start , "seconds")
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