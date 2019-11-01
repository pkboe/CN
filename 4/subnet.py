import math
ip_in_dec = input('Enter the IP address')
ip_in_dec = ip_in_dec.split('.')
ip_in_bin_list = []
for i in ip_in_dec:
	ip_in_bin = bin(int(i))
	ip_in_bin = ip_in_bin.split('b')[1]
	length = len(ip_in_bin)
	total_length = 8-length
	ip_in_bin = ('0'*total_length) + ip_in_bin
	ip_in_bin_list.append(ip_in_bin)
ip_in_bin_list='.'.join(ip_in_bin_list)
print('IP address in binary'+ip_in_bin_list)
n=int(input('Enter the no. of addresses'))
bits = math.ceil(math.log(n)/math.log(2))
print('Number of addresses required:'+ str(bits))
mask = 32-bits
print('Subnet Mask:' + str(mask))
ip_in_bin_list3 = ip_in_bin_list.split('.')[3]
ip_in_bin_list3 = list(ip_in_bin_list3)
ip_in_bin = []
for i in ip_in_bin_list3:
	ip_in_bin.append(int(i))
for i in range(8-bits,len(ip_in_bin)):
	ip_in_bin[i]=ip_in_bin[i] & 0

ip_in_bin_str = []
for i in ip_in_bin:
	ip_in_bin_str.append(str(i))

ip_in_bin_str = ''.join(ip_in_bin_str)
ip_in_bin_list = ip_in_bin_list.split('.')
subnet_address = ip_in_bin_list
subnet_address[3] = ip_in_bin_str
sub_address = []
for i in subnet_address:
	sub_address.append(str(int(i,2)))
sub_address = '.'.join(sub_address)
print('Subnet Address is:' + sub_address)

broadcast_address = ip_in_bin_list
ip_in_bin = []
for i in ip_in_bin_list3:
	ip_in_bin.append(int(i))
for i in range(8-bits,len(ip_in_bin)):
	ip_in_bin[i]=ip_in_bin[i] | 1
ip_in_bin_str = []
for i in ip_in_bin:
	ip_in_bin_str.append(str(i))

ip_in_bin_str = ''.join(ip_in_bin_str)
broadcast_address[3] = ip_in_bin_str
broad_address = []
for i in broadcast_address:
	broad_address.append(str(int(i,2)))
broad_address = '.'.join(broad_address)
print('Broadcast Address is:' + broad_address)
