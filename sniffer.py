from link_level import RawSocket, Ethernet

e = Ethernet(raw_socket=RawSocket())

for frame in e.frames():
	print(frame)