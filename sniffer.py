from link_level import RawSocket, Ethernet
from network_level import IPDatagram

e = Ethernet(raw_socket=RawSocket())

for frame in e.frames():

	if frame.type == Ethernet.Frame.IPv4_TYPE:

		ipd = IPDatagram(raw_bytes=frame.data)
		print(ipd)

