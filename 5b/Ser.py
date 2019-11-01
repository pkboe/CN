import socket
def server_program():
	host = socket.gethostname()
	port = 5001
	server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	server_socket.bind((host,port))
	server_socket.listen(2)
	conn,addr = server_socket.accept()
	data = conn.recv(1024).decode()
	print('file name is:{}'.format(data))
	with open(data,'r') as f:
		a = f.readlines()
	a= ''.join(a)
	print(a)
	conn.send(a.encode())
	conn.close()
if __name__ == '__main__':
	server_program()