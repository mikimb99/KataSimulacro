import socket
import sys

# crea un socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# enlace de socket y puerto
server_address = ('localhost', 12345)
print('Servidor escuchando en el puerto', server_address[1])
sock.bind(server_address)

# escucha conexiones entrantes
sock.listen(1)

while True:
    # espera a una conexion
    print('Esperando conexión entrante...')
    connection, client_address = sock.accept()

    try:
        print('Conexión entrante de', client_address)

        # recibe los datos del cliente
        data = connection.recv(1024)
        file_path = data.decode()
        print('Archivo recibido:', file_path)

        # procesa los datos del archivo
        with open(file_path, 'r') as file:
            if connection.recv(1024).decode() == "entero":
                file_content = file.read()
                a_count = file_content.count('a')
                print(f"El archivo contiene {a_count} letras 'a'.")
            else:
                line_count = 1
                for line in file:
                    a_count = line.count('a')
                    print(f"Línea {line_count}: {a_count}")
                    line_count += 1

        # envía confirmación al cliente
        connection.sendall(b"Archivo procesado correctamente")

    except Exception as e:
        print(e)

    finally:
        # cierra la conexión
        connection.close()
se()