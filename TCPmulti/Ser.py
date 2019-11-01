import socket
from _thread import *
host = socket.gethostname()
port = 5002
server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind((host,port))
server_socket.listen(3)
a=[]
def clientthread(conn):
	while True:
		data = conn.recv(1024).decode()
		if not data:
			break
		print(data)
		for i in a:
			if i!=conn:
				i.send(data.encode())
	conn.close()

while True:
	conn,addr = server_socket.accept()
	a.append(conn)
	start_new_thread(clientthread,(conn,))