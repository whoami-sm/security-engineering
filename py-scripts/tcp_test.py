#!/usr/bin/python3
import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(5)
print(f"Listening on {bind_ip}:{bind_port}")

def handle_thread (client_socket):
	request = client_socket.recv(1024)
	print(f"[*] Received: {bind_ip}", request)
	client_socket.close
while True:
	client, addr = server.accept()
	print("[*] Accepted connection from: {bind_ip}:{bind_port}", (addr[0], addr[1]))
	client_handler = threading.Thread(target=handle_thread,args=(client,))
	client_handler.start()
