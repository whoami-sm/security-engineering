#!/usr/bin/python3

"""Thread handling function test"""

def handle_thread (client_socket) # initialised the client_socket parameter
	request = client_socket.recv(1024) # this variable here receives 1024 bytes of data from the client socet and stores it, it will then pass it on to the client_socket parameter
	print("[*] Received: %s" % request)
	client_socket.close() # this lines closes the client socket after it receives the data
while True:
	client, addr = server.accept() # this line will accept the client address and address and pass it on to the defined parameters
	print("[*] Accepted connection from: %s:%d" % (addr[0], addr[1]))
	client_handler = threading.Thread(target=handle_thread, args=(client,))
	client_handler.start() # this line spins up the client_handler


"""So does the recv method in teh client script receive the data sent in the 
   client script and relays it to the server script?
   Why does addr[0] always remain the same and addr[1] always change
"""