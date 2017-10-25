#Cliente UDP
import socket
# Endereco IP do Servidor
SERVER = '127.0.0.1'
# Porta que o Servidor esta escutando
PORT = 5002
udp = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
dest = (SERVER, PORT)
print ('Para sair use CTRL+X\n')
msg = input()
while msg != '\x18':
    udp.sendto (msg.encode(), dest)
    msg = input()
udp.close()
