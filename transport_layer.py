import struct

#Ver também página 141 do Kurose

#Conforme página 148 do Kurose
class UDPPackage:
	def __init__(self, raw_bytes):
		self.src_port, self.dest_port, self.size = struct.unpack('! H H 2x H', raw_bytes[:8])

#Conforme página 172 do Kurose
class TCPPackage:
	def __init__(self, raw_bytes):
		self.src_port, self.dest_port, self.sequence, self.acknowledgenment, flags = struct.unpack('! H H L L H', raw_bytes[:14])
		self.offset = (flags >> 12) * 4
		self.flags = (urg, ack, psh, rst, syn, fin) = (((flags & 32) >> 5), ((flags & 32) >> 4), ((flags & 32) >> 3), ((flags & 32) >> 2), ((flags & 32) >> 1), ((flags & 32) >> 1))


