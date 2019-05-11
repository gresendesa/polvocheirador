from link_level import RawSocket, Ethernet
from network_level import IPDatagram

ethernet = Ethernet(raw_socket=RawSocket())

for frame in ethernet.frames():

	if frame.type == Ethernet.Frame.IPv4_TYPE:

		datagram = IPDatagram(raw_bytes=frame.data)
		print(datagram)

