import random
import time
arr=[]
send=[]
recv=[]
recv_ack=[]
def input1():
	n=int(input('enter no. of bits for  sequence :'))
	m=2**n
	fsai=int(m/2)
	t=0
	for i in range(0,m):
		arr.append(t)
		t=(t+1)%m
	for i in range(0,fsai):
		send.append(arr[i])
		recv.append(arr[i])
		recv_ack.append('n')
	sender(fsai,m)

def sender(fsai,m):
	for i in range(0,fsai):
		if(recv_ack[i]=='n'):
			print("SENDER : Frame {} is sent".format(send[i]))
	receiver(fsai,m)

def receiver(fsai,m):
	rw=sw=fsai
	time.sleep(1)
	a=[i for i in range(0,10)]
	for i in range(0,fsai):
		if(recv_ack[i]=='n'):
			f=random.choice(a)
			if(f!=5):
				print('frame correctly received {}'.format(recv[i]))
				a1=[k for k in range(0,5)]
				f1=random.choice(a1)
				if(f1==3):
					print("(acknowledgement {} lost)".format(send[i]))
					print('sender timeouts-->Resend the frame')
				else:	
					print("(acknowledgement {} recieved)".format(send[i]))
					recv_ack[i]='p'
			else:
				a1=[k for k in range(0,2)]	
				f2=random.choice(a1)
				if(f2==0):
					print('frame {} lost'.format(send[i]))
					print('RECEIVER : Negative Acknowledgement {} sent'.format(send[i]))
				else:
					print('frame {} damaged'.format(send[i]))
					print('(SENDER TIMEOUTS-->RESEND THE FRAME)')	
				recv_ack[i]='n'
	print('do you want to continue')
	a=input()
	if(a=='y'):
		sender(fsai,m)
	else:
		return							
input1()