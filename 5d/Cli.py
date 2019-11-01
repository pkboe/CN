import socket
def client_program():
	host = socket.gethostname()
	port = 4001
	client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	client_socket.connect((host,port))
	ch=input('1 sin\n2 cos\n3 tan\n')
	client_socket.send(ch.encode())
	ang = input('Enter the angle')
	client_socket.send(ang.encode())
	data = client_socket.recv(1024).decode()
	print(data)
	client_socket.close()
if __name__ == '__main__':
	client_program()