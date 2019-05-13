import struct

#Ver também página 141 do Kurose
#https://docs.python.org/3/library/stdtypes.html
#

#Conforme página 148 do Kurose
class SegmentoUDP:
	def __init__(self, bytes_brutos):
		self.orig_porta, self.dest_porta, self.comprimento = struct.unpack('! H H 2x H', bytes_brutos[:8])
		self.dados = bytes_brutos[8:]

#Conforme página 172 do Kurose
class SegmentoTCP:
	def __init__(self, bytes_brutos):
		self.orig_porta, self.dest_porta, self.sequencia, self.reconhecimento, comprimento_cabecalho_bruto, flags_brutos, self.janela_recepcao, self.soma_verificacao, self.ponteiro_urgencia = struct.unpack('! H H L L B B H H H', bytes_brutos[:20])
		self.comprimento_cabecalho = comprimento_cabecalho_bruto >> 4
		flags_byte = flags_brutos << 2  
		self.flags = (bool(flags_byte & 256),bool(flags_byte & 128),bool(flags_byte & 64),bool(flags_byte & 32),bool(flags_byte & 16),bool(flags_byte & 8))
		self.dados = bytes_brutos[20:]


