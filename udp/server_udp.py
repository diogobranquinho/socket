#Servidor UDP
import socket
#Endereco IP do Servidor
HOST = ''
# Porta que o Servidor vai escutar
PORT = 5002
udp = socket.socket(socket.AF_INET,
socket.SOCK_DGRAM)
orig = (HOST, PORT)
udp.bind(orig)
while True:
    msg, cliente = udp.recvfrom(1024)
    print (cliente, msg)
udp.close()
