from camada_enlace import SocketBaixoNivel, Ethernet
from camada_rede import DatagramaIP
from camada_transporte import PacoteUDP, PacoteTCP

ethernet = Ethernet(bytes_socket= SocketBaixoNivel())

for quadro in ethernet.quadros():

	if quadro.type == Ethernet.Quadro.IPv4_TYPE:

		datagrama = DatagramaIP(bytes_brutos=quadro.data)
		
		if datagrama.protocolo == DatagramaIP.TCP:

			print(PacoteTCP(bytes_brutos=datagrama.data))
		
		elif datagrama.protocolo == DatagramaIP.UDP:

			print(PacoteUDP(bytes_brutos=datagrama.data))

		else:

			print(datagrama, "type: ", datagrama.protocolo)




