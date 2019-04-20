    
"""simple TCP client."""
import socket

server_name = 'localhost'
server_port = 12000
#Cria socket do cliente. AF_INET declara IPv4 e SOCK_STREAM indica socket TCP
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#Essa linha está criando socket para handshake. Parametros em connect identificam endereço do lado do servidor da conexão
client_socket.connect((server_name, server_port))
#Realizada apresentação em 3 vias e estabelecido TCP
sentence = input('Input lowercase sentence:')
#Envia cadeia para socket 
client_socket.send(sentence.encode())
#cliente espera receber bytes de volta
modified_sentence = client_socket.recv(1024)
print('From Server: {}'.format(modified_sentence.decode()))

client_socket.close()
