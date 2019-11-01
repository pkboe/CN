import socket
def server_program():
	host = socket.gethostname()
	port = 8001
	server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	server_socket.bind((host,port))
	server_socket.listen(2)
	conn,addr = server_socket.accept()
	ch = conn.recv(1024).decode()
	a=[]
	for i in range(2):
		a.append(int(conn.recv(1024).decode()))
	print(a)
	if(ch=='+'):
		a1,a2=a
		print('Addition is:{}'.format(a1+a2))
		b=a1+a2
		conn.send(str(b).encode())
	elif(ch=='-'):
		a1,a2=a
		print('Subtraction is:{}'.format(a1-a2))
		b=a1-a2
		conn.send(str(b).encode())
	elif(ch=='*'):
		a1,a2=a
		print('Addition is:{}'.format(a1*a2))
		b=a1*a2
		conn.send(str(b).encode())
	elif(ch=='/'):
		a1,a2=a
		print('Addition is:{}'.format(a1/a2))
		b=a1/a2
		conn.send(str(b).encode())
	conn.close()	
if __name__ == '__main__':
	server_program()