import socket
import time
from funcion import Funcion

SERVER_ADDRESS = ('localhost', 10000)

serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_socket.bind(SERVER_ADDRESS)
serv_socket.listen(1)

# Crear una instancia de la clase Funcion
funcion = Funcion()

while True:
    conn, addr = serv_socket.accept()
    try:
        data = conn.recv(1024)
        option = data.decode()

        if option == 'fecha':
            fecha_actual = funcion.obtener_fecha()
            conn.send(fecha_actual.encode())
        elif option == 'hora':
            hora_actual = funcion.obtener_hora()
            conn.send(hora_actual.encode())
        else:
            conn.send('Opción inválida'.encode())

    finally:
        conn.close()
        time.sleep(1)

serv_socket.close()
