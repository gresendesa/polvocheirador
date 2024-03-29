from camada_enlace import Ethernet
from camada_rede import IP
from camada_transporte import Transporte

#Ideias das cores tiradas de https://www.geeksforgeeks.org/print-colors-python-terminal/
color = lambda color, txt='': "{}{}\033[00m".format(color, txt)

vermelho =  		lambda txt='': color(color="\033[31m", txt=txt)
verde =  			lambda txt='': color(color="\033[32m", txt=txt)
azul =  			lambda txt='': color(color="\033[34m", txt=txt)
magenta = 			lambda txt='': color(color="\033[36m", txt=txt)
white = 			lambda txt='': color(color="\033[37m", txt=txt)
vermelho_claro = 	lambda txt='': color(color="\033[91m", txt=txt)
verde_claro = 		lambda txt='': color(color="\033[92m", txt=txt)
amarelo = 			lambda txt='': color(color="\033[93m", txt=txt)
purpura_claro = 	lambda txt='': color(color="\033[94m", txt=txt)
purpura = 			lambda txt='': color(color="\033[95m", txt=txt)
ciano = 			lambda txt='': color(color="\033[96m", txt=txt)
cinza_claro = 		lambda txt='': color(color="\033[97m", txt=txt)
preto = 			lambda txt='': color(color="\033[98m", txt=txt)

fundo_preto = 		lambda txt='': color(color="\033[40m", txt=txt)
fundo_vermelho =  	lambda txt='': color(color="\033[41m", txt=txt)
fundo_verde = 		lambda txt='': color(color="\033[42m", txt=txt)
fundo_laranja = 	lambda txt='': color(color="\033[43m", txt=txt)
fundo_azul = 		lambda txt='': color(color="\033[44m", txt=txt)
fundo_purpura = 	lambda txt='': color(color="\033[45m", txt=txt)
fundo_ciano = 		lambda txt='': color(color="\033[46m", txt=txt)
fundo_cinza_claro = lambda txt='': color(color="\033[47m", txt=txt)

#Classe que representa a transformação dos dados em linhas legíveis no teminal
class FiltroInstagram:

	def __init__(self, quadro_ethernet):
		self.quadro = quadro_ethernet
		self.datagrama_IP = IP.Datagrama(bytes_brutos=self.quadro.data)

	def pormenorizar(self, numero):
		if self.quadro.type == Ethernet.Quadro.IPv4_TYPE:
			self.printar(fundo_purpura("Quadro Ethernet {}".format(numero)), recuo=0)
			self.printar(azul("MAC Origem:\t\t\t{}".format(self.quadro.dest, numero)), recuo=1)
			self.printar(azul("MAC Destino:\t\t\t{}".format(self.quadro.orig, numero)), recuo=1)
			self.mostrar_IP()
		#else:
		#	self.printar("Quadro Ethernet {} tipo {} (não IPv4)".format(numero, self.quadro.type))

	def mostrar_IP(self):
		self.printar(fundo_azul("Datagrama IPv{}".format(str(self.datagrama_IP.versao))), recuo=2)
		self.printar(purpura_claro("Tempo de vida (TTL):\t\t" + str(self.datagrama_IP.ttl)), recuo=3)
		self.printar(amarelo("Protocolo superior:\t\t{}".format('TCP' if self.datagrama_IP.protocolo == IP.Datagrama.TCP else 'UDP' if self.datagrama_IP.protocolo == IP.Datagrama.UDP else str(self.datagrama_IP.protocolo))), recuo=3)
		self.printar(verde_claro("Endereço de Origem:\t\t{} ({})".format(self.datagrama_IP.orig, IP.reverse_lookup(addr=self.datagrama_IP.orig))), recuo=3)
		self.printar(cinza_claro("Endereço de Destino:\t\t{} ({})".format(self.datagrama_IP.dest, IP.reverse_lookup(addr=self.datagrama_IP.dest))), recuo=3)
		self.printar(ciano("Tamanho dos dados:\t\t{} bytes".format(str(len(self.datagrama_IP.dados)))), recuo=3)

		if self.datagrama_IP.protocolo == IP.Datagrama.TCP:
			self.mostrar_TCP()
		elif self.datagrama_IP.protocolo == IP.Datagrama.UDP:
			self.mostrar_UDP()

	def mostrar_TCP(self):
		pacote_TCP = Transporte.SegmentoTCP(bytes_brutos=self.datagrama_IP.dados)
		self.printar(fundo_vermelho(amarelo("Segmento TCP")), recuo=4)
		self.printar(white("Porta de origem:\t\t{} {}".format(pacote_TCP.orig_porta, fundo_laranja(Transporte.apelido_porta(pacote_TCP.orig_porta, 'tcp')))), recuo=5)
		self.printar(white("Porta de destino:\t\t{} {}".format(pacote_TCP.dest_porta, fundo_laranja(Transporte.apelido_porta(pacote_TCP.dest_porta, 'tcp')))), recuo=5)
		self.printar(white("Número de sequência:\t{}".format(pacote_TCP.sequencia)), recuo=5)
		self.printar(white("Número de reconhecimento:\t{}".format(pacote_TCP.reconhecimento)), recuo=5)
		self.printar(white("Comprimento do cabecalho:\t{} palavras de 32 bits ({} bytes)".format(pacote_TCP.comprimento_cabecalho, pacote_TCP.comprimento_cabecalho * 4)), recuo=5)
		self.printar(white("Janela de recepção:\t{}".format(pacote_TCP.janela_recepcao)), recuo=5)
		self.printar(white("Soma de verificação:\t{}".format(pacote_TCP.soma_verificacao)), recuo=5)
		self.printar(white("Ponteiro de urgência:\t{} ".format(pacote_TCP.ponteiro_urgencia)), recuo=5)
		self.printar(white("Comprimento de opções:\t{} bytes".format(len(pacote_TCP.opcoes))), recuo=5)
		self.printar(white("Comprimento dos dados:\t{} bytes".format(len(pacote_TCP.dados))), recuo=5)
		self.printar(magenta("URG:{} ACK:{} PSH:{} RST:{} SYN:{} FIN:{} ".format(*pacote_TCP.flags)), recuo=5)

	def mostrar_UDP(self):
		pacote_UDP = Transporte.SegmentoUDP(bytes_brutos=self.datagrama_IP.dados)
		self.printar(fundo_ciano(vermelho("Segmento UDP")), recuo=4)
		self.printar(white("Porta de origem:\t\t{} {}".format(pacote_UDP.orig_porta, fundo_laranja(Transporte.apelido_porta(pacote_UDP.orig_porta)))), recuo=5)
		self.printar(white("Porta de destino:\t\t{} {}".format(pacote_UDP.dest_porta, fundo_laranja(Transporte.apelido_porta(pacote_UDP.dest_porta)))), recuo=5)
		self.printar(white("Comprimento do segmento:\t{} bytes".format(pacote_UDP.comprimento)), recuo=5)
		self.printar(white("Soma de verificação:\t{}".format(pacote_UDP.soma_verificacao)), recuo=5)
		self.printar(white("Comprimento dados:\t\t{} bytes".format(len(pacote_UDP.dados))), recuo=5)

	def printar(self, txt, recuo=0):
		str_recuo = ' ' * recuo
		print(str_recuo + txt)