"""simple UDP client."""

import socket
#Def do hostname e da porta
server_name = 'localhost' 
server_port = 12000
#cria socket cliente. AF_INET fala que é IPv4 - SOCK_DGRAM é socket UDP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
#Input da mensagem
message = input('Input lowercase sentence: ')
#sendto acrescenta endereço do destino - server name, server port - envia pacote
client_socket.sendto(message.encode(), (server_name, server_port))
#dados que vem da internet vão em modified e endereço de origem em server_adress
#não precisa pois temos desde o inicio, mas...
modified_message, server_address = client_socket.recvfrom(2048)


print(modified_message.decode())
client_socket.close()
