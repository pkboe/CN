import socket
ch = input('Enter the host name')
d1 = socket.gethostbyname(ch)
print(d1)
d2 = socket.gethostbyaddr(d1)
print(d2)