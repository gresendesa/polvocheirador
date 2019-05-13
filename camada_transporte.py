import struct

#Ver também página 141 do Kurose
#ver https://docs.python.org/2/library/struct.html para entender struct.unpack
#ver https://docs.python.org/3/library/stdtypes.html para entender operação envolvendo bits

#Conforme página 148 do Kurose
class SegmentoUDP:
	def __init__(self, bytes_brutos):
		self.orig_porta, self.dest_porta, self.comprimento = struct.unpack('!H H 2x H', bytes_brutos[:8])
		self.dados = bytes_brutos[8:]

#Conforme página 172 do Kurose
class SegmentoTCP:
	def __init__(self, bytes_brutos):
		self.orig_porta, self.dest_porta, self.sequencia, self.reconhecimento, flags = struct.unpack('! H H L L H', bytes_brutos[:14])
		self.offset = (flags >> 12) * 4
		self.flags = (urg, ack, psh, rst, syn, fin) = ((flags & 20), (flags & 10), (flags & 8), (flags & 4), (flags & 2), (flags & 1))
		self.dados = bytes_brutos[self.offset:]