#!/usr/bin/python3
from socket import *
s = socket(AF_INET, SOCK_STREAM)
s.connect(("127.0.0.1", 22))
answer = s.recv(1024)
print(answer)
s.close # this script is client calling on port 22 (SSH server)
