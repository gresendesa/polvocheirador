from camada_enlace import SocketBaixoNivel, Ethernet
from camada_rede import IP
from embelezador_IP import FiltroInstagram

socket = SocketBaixoNivel()
ethernet = Ethernet(bytes_socket=socket)

try:

	for quadro in ethernet.quadros():

		if quadro.type == Ethernet.Quadro.IPv4_TYPE:

			datagrama = IP.Datagrama(bytes_brutos=quadro.data)

			FiltroInstagram(datagrama_IP=datagrama).mostrar_IP(numero=ethernet.contador_quadros)

except KeyboardInterrupt:

	socket.fechar()

	print("\nPolvoCheirador fechou o socket! Programa finalizado")
