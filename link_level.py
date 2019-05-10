import socket
import struct

#Classe que representa o socket configurado para capturar pacotes de baixo nível
class RawSocket:
	def __init__(self):
		self.conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

	#Extrai bufsize bytes do socket
	def read(self):
		return self.conn.recvfrom(bufsize=65536)

#Classe que representa a camada de enlace
class Ethernet:
	def __init__(self, raw_socket):
		self.raw_socket = raw_socket
		self.data = b''
		self.addr = b''
		
	#Lê bytes do socket na ordem de transmissão. Dados crus	
	def capture_bytes(self):
		self.data, self.addr = self.raw_socket.read()

	#Interpreta bytes do socket conforme a estrutura mostrada na página 349 do Kurose
	def get_frame(self):
		self.capture_bytes()
		dest_mac, src_mac, type = struct.unpack('! 6s 6s H', self.data[:14])
		return Ethernet.Frame(self.stringify_mac_addr(dest_mac), self.stringify_mac_addr(src_mac), socket.htons(type), self.data[14:])

	#Implementa um gerador para ser iterado no for
	def frames(self):
		while 1:
			yield self.get_frame()

	#Torna  mac de bytes para string
	def stringify_mac_addr(self, bytes_addr):
		str_addr = map('{:02x}'.format, bytes_addr)
		return ':'.join(str_addr).upper()

	#Classe que representa um quadro Ethernet (da camada de enlace)
	class Frame:
		def __init__(self, dest, src, type, data):
			self.dest = dest
			self.src = src
			self.type = type
			self.data = data