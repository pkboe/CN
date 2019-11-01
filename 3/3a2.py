import time
import socket
def client_program():
	host = socket.gethostname()
	port=5001
	client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	client_socket.connect((host,port))
	n=input('enter no. of frames to be sent ')
	client_socket.send(n.encode())
	e=input('enter 1=error 2=noerror ')
	client_socket.send(e.encode())
	if(int(e)==2):
		for j in range(int(n)):
			i=client_socket.recv(1024).decode()
			print("received frame no: {}".format(i))
			client_socket.send(i.encode())
			print("Sending acknowledgement for frame no: {}".format(i))
	else:
		f=int(client_socket.recv(1024).decode())
		print(f)

		for j in range(int(n)):
			if(f!=j):
				i=client_socket.recv(1024).decode()
				print("received frame no: {}".format(i))
				client_socket.send(i.encode())
				print("Sending acknowledgement for frame no: {}".format(i))
			else:
				i=client_socket.recv(1024).decode()
				print("damaged frame no: {}".format(i))
				print("Sending negative acknowledgement for frame no: {}".format(i))

		for i in range(f,int(n)):
			i=client_socket.recv(1024).decode()
			print("received frame no: {}".format(i))
			client_socket.send(i.encode())
			print("Sending acknowledgement for frame no: {}".format(i))

	print('quitting')
	client_socket.close()

if __name__ == '__main__':
	client_program()