#Ideias tiradas de https://www.geeksforgeeks.org/print-colors-python-terminal/

vermelho = 			lambda txt: "\033[91m {}\033[00m" .format(txt) 
verde = 			lambda txt: "\033[92m {}\033[00m" .format(txt)
amarelo = 			lambda txt: "\033[93m {}\033[00m" .format(txt)
purpura_claro = 	lambda txt: "\033[94m {}\033[00m" .format(txt) 
purpura = 			lambda txt: "\033[95m {}\033[00m" .format(txt)
ciano = 			lambda txt: "\033[96m {}\033[00m" .format(txt)
cinza_claro = 		lambda txt: "\033[97m {}\033[00m" .format(txt)
preto = 			lambda txt: "\033[98m {}\033[00m" .format(txt)

fundo_preto = 		lambda txt: "\033[40m {}\033[00m" .format(txt)
fundo_vermelho =  	lambda txt: "\033[41m {}\033[00m" .format(txt)
fundo_verde = 		lambda txt: "\033[42m {}\033[00m" .format(txt)
fundo_laranja = 	lambda txt: "\033[43m {}\033[00m" .format(txt)
fundo_azul = 		lambda txt: "\033[44m {}\033[00m" .format(txt)
fundo_purpura = 	lambda txt: "\033[45m {}\033[00m" .format(txt)
fundo_ciano = 		lambda txt: "\033[46m {}\033[00m" .format(txt)
fundo_cinza_claro = lambda txt: "\033[47m {}\033[00m" .format(txt)


class FiltroInstagram:

	def __init__(self, datagrama_ip):
		self.datagrama_ip = datagrama_ip

	def mostrar_IP(self):
		print(ciano("Versao: " + str(self.datagrama_ip.versao)))
		print(purpura("Tamanho do cabecalho " + str(self.datagrama_ip.tam_cabecalho)))
		print(purpura_claro("Tempo de vida (TTL): " + str(self.datagrama_ip.ttl)))
		print(amarelo("Procolo: " + str(self.datagrama_ip.protocolo)))
		print(verde("Endereco de Origem: " + self.datagrama_ip.orig))
		print(vermelho("Endereco de Destino: " + self.datagrama_ip.dest))
		print("Dados: " + str(self.datagrama_ip.data))
		pass

	def mostrar_TCP(self):
		print(ciano("Versao: " + str(self.datagrama_ip.versao)))
		print(purpura("Tamanho do cabecalho " + str(self.datagrama_ip.tam_cabecalho)))
		print(purpura_claro("Tempo de vida (TTL): " + str(self.datagrama_ip.ttl)))
		print(amarelo("Procolo: " + str(self.datagrama_ip.protocolo)))
		print(verde("Endereco de Origem: " + self.datagrama_ip.orig))
		print(vermelho("Endereco de Destino: " + self.datagrama_ip.dest))
		print("Dados: " + str(self.datagrama_ip.data))
		pass

	def mostrar_UDP(self):
		print(ciano("Versao: " + str(self.datagrama_ip.versao)))
		print(purpura("Tamanho do cabecalho " + str(self.datagrama_ip.tam_cabecalho)))
		print(purpura_claro("Tempo de vida (TTL): " + str(self.datagrama_ip.ttl)))
		print(amarelo("Procolo: " + str(self.datagrama_ip.protocolo)))
		print(verde("Endereco de Origem: " + self.datagrama_ip.orig))
		print(vermelho("Endereco de Destino: " + self.datagrama_ip.dest))
		print("Dados: " + str(self.datagrama_ip.data))
		pass