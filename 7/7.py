import socket
import struct

def main():
	ser=socket.socket(socket.AF_PACKET,socket.SOCK_RAW,socket.ntohs(3))
	while True:
		raw_data,addr=ser.recvfrom(65536)
		desc_mac,src_mac,pro_type,data= ethernet(raw_data)
		print('Ethernet:\n Destination MAC Address:{} \n Source MAC Address:{}\n Protocol: {}\n'.format(desc_mac,src_mac,pro_type))
		if pro_type==8:
			version,headerlen,ttl,pro_type1,src,desc,data = ipv4_header(raw_data)
			print('IPv4:\nVersion:{} \n Header length: {} \n Time To Live:{}\n Protocol: {}\n Source Address:{}\n Destination Address:{} \n Data:{}\n'.format(version,headerlen,ttl,pro_type1,src,desc,data))
			if pro_type1==1:
				Type,code,checksum,data=ICMP(raw_data)
				print('ICMP:\nType:{}\nCode:{}\n Checksum:{}\nData:{}\n'.format(Type,code,checksum,data))
			elif pro_type1==6:
				src_port,dest_port,sequence,ack,offset,data=TCP(data)
				print('TCP:\nSource Port:{}\nDestination Port:{}\nSequence:{}\nAcknowledgement:{}\nOffset:{}\nData:{}\n'.format(src_port,dest_port,sequence,ack,offset,data))
			elif pro_type1==17:
				src_port,dest_port,size,data=UDP(data)
				print('UDP:\nSource Port:{}\nDestination Port:{}\nSize:{}\nData:{}\n'.format(src_port,dest_port,size,data))
def ethernet(data):
	desc_mac,src_mac,pro_type=struct.unpack('! 6s 6s H',data[:14])
	return ethProperFormat(desc_mac),ethProperFormat(src_mac),socket.htons(pro_type),data[14:]

def ethProperFormat(addr):
	addr=map('{:02x}'.format,addr)
	return ':'.join(addr).upper()

def ipv4_header(data):
	version_headerlen=data[0]
	version=version_headerlen >> 4
	headerlen= (version_headerlen & 15)*4
	ttl,pro_type,src,desc= struct.unpack('! 8x B B 2x 4s 4s',data[:20])
	return version,headerlen,ttl,pro_type,ipProperFormat(src),ipProperFormat(desc),data[20:]

def ipProperFormat(addr):
	return '.'.join(map(str,addr))

def  ICMP(data):
	Type,code,checksum = struct.unpack('! B B H',data[:4])
	return Type,code,checksum,data[4:]

def TCP(data):
	src_port,dest_port,sequence,ack,offset_reserved_flag = struct.unpack('! H H L L H',data[:14])
	offset = (offset_reserved_flag >> 12) * 4
	return src_port,dest_port,sequence,ack,offset,data[offset:]

def UDP(data):
	src_port,dest_port,size = struct.unpack('!H H 2x H',data[:8])
	return src_port,dest_port,size,data[8:]
if __name__ == '__main__':
	main()