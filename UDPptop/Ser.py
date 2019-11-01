import socket
def server_program():
	host = socket.gethostname()
	port = 4500
	server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	server_socket.bind((host,port))
	while True:
		data,addr = server_socket.recvfrom(1024)
		print(data.decode())
		if not data.decode():
			break
		msg = input('-->')
		server_socket.sendto(msg.encode(),addr)
	server_socket.close()
if __name__ == '__main__':
	server_program()