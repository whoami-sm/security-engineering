#!/usr/bin/python3
import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# solves the "Address already in use" error if you restart the server quickly
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((bind_ip, bind_port))
server.listen(5)
print("[*] Listening on %s:%d" % (bind_ip, bind_port))


"""the thread handler function is used to handle multiple concurrent requests at the same time"""
def handle_thread(client_socket):
	try:
		request = client_socket.recv(1024)

		# check if the client closed the connection without sending data
		if not request:
			print("[*] Client disconnected immediately.")
			return
		# safely decode ignoring invalid non-text characters
		decode_request = request.decode("utf-8", errors = "ignore")
		print("[*] Received: %s" % request.decode())
		# send a response back to client so it does not just get an empty closure
		ack_message = "Data received successfully!"
		client_socket.send(ack_message.encode("utf-8"))
	except Exception as e:
		print(f"[-] Error handling client: {e}")
	finally:
		# crucial: Always ensure the socket closes even if an error occurs
		client_socket.close()

while True:
	try:
		client, addr = server.accept()
		print("[*] Accepted connection from: %s:%d" % (addr[0], addr[1]))
		client_handler = threading.Thread(target=handle_thread,args=(client,))
		client_handler.start()
	except KeyboardInterrupt:
		print("\n[*] Shutting down server.")
		break
	except Exception as e:
		print(f"[-] Server loop error: {e}")
