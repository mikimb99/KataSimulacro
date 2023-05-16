import socket
import sys
import time
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 12345)
filepath = input('Introduce el path del fichero: ')

# Verifica si el archivo existe
try:
    with open(filepath, 'r') as f:
        pass
except FileNotFoundError:
    print("El archivo especificado no existe.")
    sys.exit()

client_socket.connect(server_address)

# Una vez comprobado que el path existe, lo imprimo en el cliente
# ESPERA LA RESPUESTA
try:
    # envia el path del fichero
    client_socket.sendall(filepath.encode())

    # recibe los datos del archivo en bloques de 1024
    data = b''
    while True:
        chunk = client_socket.recv(1024)
        if not chunk:
            break
        data += chunk
    # convierte las letras 'a' y 'A' en minúsculas
    data = data.decode().replace('A', 'a')
    # cuenta el número de letras 'a' en el archivo
    num_a = data.count('a')
    # imprime el resultado
    print(f"El archivo contiene {num_a} letras 'a'.")
    print(data)

finally:
    time.sleep(1)
    client_socket.close()