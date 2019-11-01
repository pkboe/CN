import socket
def client_program():
	host = socket.gethostname()
	port = 8003
	client_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	fn = input('Enter the filename ')
	client_socket.sendto(fn.encode(),(host,port))
	with open(fn,'r') as f:
		a = f.readlines()
	a = ''.join(a)
	print(a)
	client_socket.sendto(a.encode(),(host,port))
	data,addr = client_socket.recvfrom(1024)
	print(data.decode())
	client_socket.close()
if __name__ == '__main__':
	client_program()
