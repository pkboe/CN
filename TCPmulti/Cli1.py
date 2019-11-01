import socket
def client_program():
	host = socket.gethostname()
	port = 5002
	client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	client_socket.connect((host,port))
	while True:
		msg = input('-->')
		client_socket.send(msg.encode())
		if msg=='bye':
			break
		data = client_socket.recv(1024).decode()
		if data=='bye':
			break
		print(data)
	client_socket.close()

if __name__ == '__main__':
	client_program()