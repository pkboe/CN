import socket
def client_program():
	host = socket.gethostname()
	port = 5001
	client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	client_socket.connect((host,port))
	fn = input('Enter the filename:')
	client_socket.send(fn.encode())
	data = client_socket.recv(1024).decode()
	print(data)
	client_socket.close()

if __name__ == '__main__':
	client_program()