import socket
import re
from funciones import Funcion

server_address = ('localhost', 12345)
print('Servidor escuchando en el puerto', server_address[1])

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(server_address)

funcion = Funcion()


while True:
    print('Esperando conexión entrante...')
    data, client_address = sock.recvfrom(1024)
    frase = data.decode('utf-8')

    print('Frase recibida:', frase)
    #para tener en cuenta 1 , y varios espacios
    palabras = re.split(r'\s*,\s*|\s+', frase)
    if all(word.isdigit() for word in palabras):
        capicuas = funcion.capicuas(frase)
        response = f"La frase contiene: {len(capicuas)} numeros capicuas:\n"
        for n in capicuas:
            response += n + "\n"
    elif all(re.match(r'^[a-zA-Z]+$',word) for word in palabras):
         a_count = funcion.count_a(frase)
         palindromas = funcion.palindromas(frase)
         response = f"La frase contiene {a_count} letras 'a'.\n"
         response += f"La frase contiene {len(palindromas)} palabras palíndromas:\n"
         for p in palindromas:
            response += p + "\n"
    else:
        response = "La entrada no se reconoce"
    sock.sendto(response.encode('utf-8'), client_address)