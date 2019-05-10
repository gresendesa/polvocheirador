import struct

#Classe que representa a camada de rede
class IPDatagram:

	def __init__(self, raw_bytes):
		self.version = raw_bytes[0] >> 4
		self.header_len = (raw_bytes[0] & 15) * 4
		self.ttl, self.proto, self.raw_src, self.raw_target = struct.unpack('! 8x B B 2x 4s 4s', raw_bytes[:20])
		self.src = self.stringfy_addr(self.raw_src)
		self.target = self.stringfy_addr(self.raw_target)
		self.data = raw_bytes[self.header_len:]

	def stringfy_addr(self, addr):
		return '.'.join(map(str, addr))



	