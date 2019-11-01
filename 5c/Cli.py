import socket
def client_program():
	host = socket.gethostname()
	port = 8001
	client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	client_socket.connect((host,port))
	ch = input('+ add\n- sub\n* mul\n/ div')
	client_socket.send(ch.encode())
	print('Enter the operands:')
	for i in range(2):
		a=input()
		client_socket.send(a.encode())
	data = client_socket.recv(1024).decode()
	print(data)
	client_socket.close()

if __name__ == '__main__':
	client_program()