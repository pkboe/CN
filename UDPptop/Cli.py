import socket
def client_program():
	host = socket.gethostname()
	port = 4500
	client_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	while True:
		msg = input('-->')
		if msg == 'bye':
			break
		client_socket.sendto(msg.encode(),(host,port))
		data,addr = client_socket.recvfrom(1024)
		print(data.decode())
	client_socket.close()
if __name__ == '__main__':
	client_program()