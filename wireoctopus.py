from link_level import RawSocket, Ethernet
from network_level import IPDatagram
from transport_layer import UDPPackage, TCPPackage

ethernet = Ethernet(raw_socket=RawSocket())

for frame in ethernet.frames():

	if frame.type == Ethernet.Frame.IPv4_TYPE:

		datagram = IPDatagram(raw_bytes=frame.data)
		
		if datagram.proto == IPDatagram.TCP:

			print(TCPPackage(raw_bytes=datagram.data))
		
		elif datagram.proto == IPDatagram.UDP:

			print(UDPPackage(raw_bytes=datagram.data))

		else:

			print(datagram, "type: ", datagram.proto)




