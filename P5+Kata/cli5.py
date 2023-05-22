import socket
import sys

server_address = ('localhost', 12345)
frase = input('Introduce una frase: ')

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
frase = frase.encode('utf-8')
try:
    client_socket.sendto(frase, server_address)

    data, _ = client_socket.recvfrom(1024)
    response = data.decode('utf-8')

    print(response)

finally:
    client_socket.close()
