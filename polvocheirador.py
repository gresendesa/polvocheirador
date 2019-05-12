from camada_enlace import SocketBaixoNivel, Ethernet
from camada_rede import DatagramaIP
from camada_transporte import PacoteUDP, PacoteTCP
from embelezador_ip import FiltroInstagram

ethernet = Ethernet(bytes_socket= SocketBaixoNivel())

for quadro in ethernet.quadros():

	if quadro.type == Ethernet.Quadro.IPv4_TYPE:

		datagrama = DatagramaIP(bytes_brutos=quadro.data)

		FiltroInstagram(datagrama_ip = datagrama).mostrar_IP()