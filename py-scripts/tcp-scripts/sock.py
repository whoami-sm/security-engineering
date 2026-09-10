#!/usr/bin/python3
""" 
 Creating clients and servers (tcp)
 This is a tcp client connected to a google.com server
"""

import socket
target_host = "altaria.proxy.rlwy.net:56680" 
target_port = 9999 

# creating a socket object, establishing the tcp client with a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # connecting the client to the server
    client.connect((target_host, target_port))
    print(f"[*] Connected to server at {target_host}:{target_port}")
    # sending some data
    client.send("Hello Server! ".encode("utf-8"))
    # recieve server's acknoledgement
    response = client.recv(1024)
    if response:
        print("[-] Server closed the connection without responding.")
    else:
        print("[-] Sevre closed the connection withput responding.")
except Exception as e:
    print(f"[-] Connection failed: {e}")
finally:
    client.close()



