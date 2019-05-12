import struct

#Classe que representa a camada de rede
class IPDatagram:

	TCP = 6
	UDP = 17

	def __init__(self, bytes_brutos):
		self.versao = bytes_brutos[0] >> 4
		self.tam_cab = (bytes_brutos[0] & 15) * 4
		self.ttl, self.proto, self.orig_bruto, self.dest_bruto = struct.unpack('! 8x B B 2x 4s 4s', bytes_brutos[:20])
		self.orig = self.stringfy_endr(self.orig_bruto)
		self.dest = self.stringfy_endr(self.dest_bruto)
		self.data = bytes_brutos[self.tam_cab:]

	def stringfy_endr(self, endr):
		return '.'.join(map(str, endr))



	