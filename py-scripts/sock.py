#!/usr/bin/python3
""" 
 Creating clients and servers (tcp)
 This is a tcp client connected to a google.com server
"""
import socket
target_host = "127.0.0.1" 
target_port = 9999 

# creating a socket object, establishing the tcp client with a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connecting the client to the server
client.connect((target_host, target_port))

# sending some data
client.send("Hello Server! ".encode())


# recieve some data
response = client.recv(1024)

print(response.decode())


