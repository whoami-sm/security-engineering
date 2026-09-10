#!/usr/bin/python3

"""Thread handling function test"""

def handle_thread (client_socket) # initialised the client_socket parameter
	request = client_socket.recv(1024)
	print("[*] Received: %s" % request)
	client_socket.close()
while True:
	
