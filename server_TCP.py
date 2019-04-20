"""simple TCP server."""

import socket
import time
import signal
import sys


def signal_handler(signal, frame):
    global server_socket
    print('\nClosing socket...')
    server_socket.close()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

server_port = 12000
#Criando socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
#Associando numero de porta do servidor ao socket
server_socket.bind(('', server_port))
#Fica escutando ate ser enviado algo
server_socket.listen(2)

print('The server is ready to receive')

cont = 0
while True:
    #Servidor escuta req TCP do cliente, acionando accept quando ouve algo
    connection_socket, addr = server_socket.accept()
    sentence = connection_socket.recv(1024)
    print('Message {} received: {}'.format(cont, sentence.decode()))
    capitalized_sentence = sentence.upper()
    # time.sleep(0.5)
    connection_socket.send(capitalized_sentence)
    connection_socket.close()
    cont += 1
