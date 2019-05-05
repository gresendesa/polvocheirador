import socket 

host  = '127.0.0.1'

s = socket.socket(socket.AF_PACKET,socket.SOCK_RAW,socket.ntohs(0x0800))

while True:
	pacote  =  s.recvfrom(65565)
	print (pacote)
