from link_level import RawSocket, Ethernet

e = Ethernet(socket=RawSocket())

for frame in e.frames():
	print(frame)