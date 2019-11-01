import socket
def server_program():
	host = socket.gethostname()
	port = 8000
	server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	server_socket.bind((host,port))
	server_socket.listen(2)
	conn,addr = server_socket.accept()
	while True:
		data = conn.recv(1024).decode()
		if not data:
			break
		print(data)
		msg = input('-->')
		conn.send(msg.encode())
	conn.close()
if __name__ == '__main__':
	server_program()