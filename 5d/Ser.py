import socket
import math
def server_program():
	host = socket.gethostname()
	port = 4001
	server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	server_socket.bind((host,port))
	server_socket.listen(2)
	conn,addr = server_socket.accept()
	ch = int(conn.recv(1024).decode())
	ang = int(conn.recv(1024).decode())
	ang = ((math.pi*ang)/180)
	if (ch==1):
		res = math.sin(ang)
		print(res)
		conn.send(str(res).encode())
	elif (ch==2):
		res = math.cos(ang)
		print(res)
		conn.send(str(res).encode())
	elif (ch==3):
		res = math.math(ang)
		print(res)
		conn.send(str(res).encode())
	conn.close()

if __name__ == '__main__':
	server_program()