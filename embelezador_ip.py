from camada_rede import IP
from camada_transporte import SegmentoTCP, SegmentoUDP

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

	def __init__(self, datagrama_IP):
		self.datagrama_IP = datagrama_IP

	def mostrar_IP(self, numero):
		self.printar(fundo_azul("Datagrama IPv{}, do quadro Ethernet {}".format(str(self.datagrama_IP.versao), numero)))
		self.printar(purpura_claro("Tempo de vida (TTL):\t\t" + str(self.datagrama_IP.ttl)), recuo=1)
		self.printar(amarelo("Protocolo da camada superior:\t{}".format('TCP' if self.datagrama_IP.protocolo == IP.Datagrama.TCP else 'UDP' if self.datagrama_IP.protocolo == IP.Datagrama.UDP else str(self.datagrama_IP.protocolo))), recuo=1)
		self.printar(verde_claro("Endereço de Origem:\t\t{} ({})".format(self.datagrama_IP.orig, IP.reverse_lookup(addr=self.datagrama_IP.orig))), recuo=1)
		self.printar(cinza_claro("Endereço de Destino:\t\t{} ({})".format(self.datagrama_IP.dest, IP.reverse_lookup(addr=self.datagrama_IP.dest))), recuo=1)
		self.printar(ciano("Tamanho dos dados:\t\t" + str(len(self.datagrama_IP.dados))), recuo=1)

		if self.datagrama_IP.protocolo == IP.Datagrama.TCP:
			self.mostrar_TCP()
		elif self.datagrama_IP.protocolo == IP.Datagrama.UDP:
			self.mostrar_UDP()

	def mostrar_TCP(self):
		pacote_TCP = SegmentoTCP(bytes_brutos=self.datagrama_IP.dados)
		self.printar(fundo_vermelho(amarelo("Segmento TCP")), recuo=3)
		self.printar(white("Porta de origem: {}".format(pacote_TCP.orig_porta)), recuo=4)
		self.printar(white("Porta de destino: {}".format(pacote_TCP.dest_porta)), recuo=4)
		self.printar(white("Número de sequência: {}".format(pacote_TCP.sequencia)), recuo=4)
		self.printar(white("Número de reconhecimento: {}".format(pacote_TCP.reconhecimento)), recuo=4)
		self.printar(white("Comprimento do cabecalho: {} palavras de 32 bits".format(pacote_TCP.comprimento_cabecalho)), recuo=4)
		self.printar(white("Flags: URG:{} ACK:{} PSH:{} RST:{} SYN:{} FIN:{} ".format(*pacote_TCP.flags)), recuo=4)
		self.printar(white("Soma de verificação: {}".format(pacote_TCP.soma_verificacao)), recuo=4)
		self.printar(white("Ponteiro de urgência: {} ".format(pacote_TCP.ponteiro_urgencia)), recuo=4)
		self.printar(white("Comprimento do campo de opções: {}".format(len(pacote_TCP.opcoes))), recuo=4)
		self.printar(white("Comprimento dos dados: {}".format(len(pacote_TCP.dados))), recuo=4)

	def mostrar_UDP(self):
		pacote_UDP = SegmentoUDP(bytes_brutos=self.datagrama_IP.dados)
		self.printar(fundo_ciano(vermelho("Segmento UDP")), recuo=3)
		self.printar(white("Porta de origem: {}".format(pacote_UDP.orig_porta)), recuo=4)
		self.printar(white("Porta de destino: {}".format(pacote_UDP.dest_porta)), recuo=4)
		self.printar(white("Comprimento do segmento inteiro: {}".format(pacote_UDP.comprimento)), recuo=4)
		self.printar(white("Soma de verificação: {}".format(pacote_UDP.soma_verificacao)), recuo=4)
		self.printar(white("Comprimento dados: {}".format(len(pacote_UDP.dados))), recuo=4)

	def printar(self, txt, recuo=0):
		str_recuo = ' ' * recuo
		print(str_recuo + txt)