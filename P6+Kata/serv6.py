import socket
from funciones import Funcion
# crea un socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
funcion = Funcion()
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
        #recibe el tipo de conteo que desea realizar
        tipo_count = connection.recv(1024).decode()
        # procesa los datos del archivo
        with open(file_path, 'r') as file:
            if tipo_count == "entero":
                file_content = file.read()
                a_count = file_content.count('a')
                print(f"El archivo contiene {a_count} letras 'a'.")
            elif tipo_count =="linea":
                line_count = 1
                for line in file:
                    a_count = line.count('a')
                    print(f"Línea {line_count}: {a_count}")
                    line_count += 1
            elif tipo_count == "palindromas":
                palindromo= funcion.palindromas(file_path)
                print(f"El archivo contiene {len(palindromo)} palabras palíndromas:")
                for p in palindromo:
                    print(p)

        # envía confirmación al cliente
        connection.sendall(b"Archivo procesado correctamente")

    except Exception as e:
        print(e)

    finally:
        # cierra la conexión
        connection.close()