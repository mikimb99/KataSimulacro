import socket
import sys
import time
from funciones import Funcion

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 12345)
filepath = input('Introduce el path del fichero: ')
tipo_count = input('Si desea contar todas las as del archivo("entero") si desea por línea ("linea")')

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
    time.sleep(0.1)
    client_socket.sendall(tipo_count.encode())
    # recibe la confirmación de que el archivo existe
    confirmation = client_socket.recv(1024).decode()
    print(confirmation)
    if not confirmation:
        print('No se ha recibido confirmación')
        sys.exit()
    #creamos una instancia de Funcion
    func = Funcion()

    if tipo_count == 'entero':

        # cuenta el número de letras 'a' en el archivo
        num_a = func.count_a(filepath)
        # imprime el resultado
        print(f"El archivo contiene {num_a} letras 'a'.")
    elif tipo_count == 'linea':
  # cuenta el número de letras 'a' en cada línea
        line_a_count = func.count_a_linea(filepath)
        # suma el número de letras 'a' en todas las líneas
        num_a = sum(line_a_count)

        # Imprime el número de letras 'a' en cada línea
        for i, count in enumerate(line_a_count):
            print(f"Línea {i+1}: {count}")

finally:
    time.sleep(1)
    client_socket.close()
