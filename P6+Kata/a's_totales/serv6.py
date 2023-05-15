import socket
import time

#FUNCIÓN PARA CONTAR LAS LETRAS A'S EN UN ARCHIVO
serv_socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 12345)
serv_socket.bind(server_address)
serv_socket.listen(1)
print('Esperando conexiones entrantes...')
while True:
    # espera una conexión entrante
    client_socket, client_address = serv_socket.accept()
    print('Conexión entrante de', client_address)

    try:
        # recibe el path del archivo del cliente
        file_path = client_socket.recv(1024).decode()
        # intenta abrir el archivo especificado por el path, si existe lo lee, sino salta el error
        with open(file_path, 'r') as file:
            data = file.read()
            # convierte las letras 'a' y 'A' en minúsculas
            data = data.replace('A', 'a')
            print(data, client_address)
            # después de leerlo lo codifica a formato bytes para volverlo a enviar
            client_socket.sendall(data.encode())

    except FileNotFoundError:
        client_socket.sendall('El archivo no existe '.encode())

    finally:
        # cierra la conexión del cliente
        client_socket.close()