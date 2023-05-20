import socket
import time

SERVER_ADDRESS = ('localhost', 10000)

while True:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    time.sleep(1)
    try:
        client_socket.connect(SERVER_ADDRESS)
    except FileNotFoundError:
        # El archivo del socket aún no está disponible, intentarlo más tarde
        continue

    # Solicitar al usuario si desea recibir la fecha o la hora
    choice = input("Ingrese 'fecha' o 'hora' para recibir la información: ")

    # Enviar la elección al servidor
    client_socket.send(choice.encode())

    # Recibir y procesar la respuesta del servidor
    data = client_socket.recv(1024).decode()

    if choice.lower() == 'fecha':
        print('Fecha recibida del servidor:', data)
    elif choice.lower() == 'hora':
        print('Hora recibida del servidor:', data)
    else:
        print('Elección inválida.')

    client_socket.close()

