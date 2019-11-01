import socket
def server_program():
	host = socket.gethostname()
	port = 8003
	server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	server_socket.bind((host,port))
	data,addr = server_socket.recvfrom(1024)
	print(data.decode())

	data,addr=server_socket.recvfrom(1024)
	with open('t1.txt','w') as f:
		f.write(data.decode())
	count = str(len(data.decode()))
	server_socket.sendto(count.encode(),addr)
	print(count)
	server_socket.close()

if __name__ == '__main__':
	server_program()
