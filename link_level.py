import socket
import struct

#Classe que representa o socket configurado para capturar pacotes de baixo nível
class RawSocket:
	def __init__(self):
		self.conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

	#Extrai bufsize bytes do socket
	def le(self):
		return self.conn.recvfrom(65536)

#Classe que representa a camada de enlace
class Ethernet:

	def __init__(self, bytes_socket):
		self.bytes_socket = bytes_socket
		self.conteudo_bytes = b''
		self.endr = b''
		
	#Lê bytes do socket na ordem de transmissão. Dados crus	
	def captura_bytes(self):
		self.conteudo_bytes, self.endr = self.bytes_socket.le()

	#Interpreta bytes do socket conforme a estrutura mostrada na página 349 do Kurose
	def get_frame(self):
		self.captura_bytes()
		dest_mac, orig_mac, type = struct.unpack('! 6s 6s H', self.conteudo_bytes[:14])
		return Ethernet.Frame(self.stringify_mac_endr(dest_mac), self.stringify_mac_endr(orig_mac), socket.htons(type), self.conteudo_bytes[14:])

	#Implementa um gerador para ser iterado no for (https://bit.ly/2HdCRHj)
	def frames(self):
		while 1:
			yield self.get_frame()

	#Torna  mac de bytes para string
	def stringify_mac_endr(self, bytes_endr):
		str_endr = map('{:02x}'.format, bytes_endr)
		return ':'.join(str_endr).upper()

	#Classe que representa um quadro Ethernet (da camada de enlace)
	class Frame:

		IPv4_TYPE = 8

		def __init__(self, dest, orig, type, data):
			self.dest = dest
			self.orig = orig
			self.type = type
			self.data = data