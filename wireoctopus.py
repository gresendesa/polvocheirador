from link_level import RawSocket, Ethernet
from network_level import IPDatagram
from transport_layer import UDPPackage, TCPPackage

ethernet = Ethernet(bytes_socket= RawSocket())

for frame in ethernet.frames():

	if frame.type == Ethernet.Frame.IPv4_TYPE:

		datagram = IPDatagram(bytes_brutos=frame.data)
		
		if datagram.proto == IPDatagram.TCP:

			print(TCPPackage(bytes_brutos=datagram.data).orig_port)
		
		elif datagram.proto == IPDatagram.UDP:

			print(UDPPackage(bytes_brutos=datagram.data).orig_port)

		else:

			print(datagram, "type: ", datagram.proto)




