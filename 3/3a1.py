import socket
import time
import random
def server_program():
	host = socket.gethostname()
	port=5001
	server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	server_socket.bind((host,port))
	server_socket.listen(2)
	conn,addr = server_socket.accept()
	n=int(conn.recv(1024).decode())
	print(n)
	e=int(conn.recv(1024).decode())
	print(e)
	a=[i for i in range(n)]
	f=random.choice(a)
	if(e==2):
		for i in range(n):
			print("sending frame number {}".format(i))
			conn.send(str(i).encode())
			print("Waiting for acknowledgement")
			time.sleep(3)
			a = conn.recv(1024).decode()
			print("received acknowledgement for frame {} as {}".format(i,a))
	else:
		conn.send(str(f).encode())
		print(f)
		for i in range(n):
			if(f!=i):
				print("sending frame number {}".format(i))
				conn.send(str(i).encode())
				print("Waiting for acknowledgement")
				time.sleep(3)
				a = conn.recv(1024).decode()
				print("received acknowledgement for frame {} as {}".format(i,a))
			else:
				print("sending frame number {}".format(i))
				conn.send(str(i).encode())
				print("Waiting for acknowledgement")
				time.sleep(3)

		for i in range(f,n):
			print("resending frame number {}".format(i))
			conn.send(str(i).encode())
			print("Waiting for acknowledgement")
			time.sleep(3)
			a = conn.recv(1024).decode()
			print("received acknowledgement for frame {} as {}".format(i,a))
	print('quitting')

	conn.close()
if __name__ == '__main__':
	server_program()