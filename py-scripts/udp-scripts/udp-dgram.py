from socket import *
s = socket(AF_INET, SOCK_DGRAM)
s.connect(("127.0.0.1", 53))
answer = s.recv(1024)
print(answer)
s.close