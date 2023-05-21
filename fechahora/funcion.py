import time

class Funcion:
    def obtener_fecha(self):
        return time.strftime("%Y-%m-%d", time.gmtime())

    def obtener_hora(self):
        return time.strftime("%H:%M:%S", time.gmtime())

# Crear una instancia de la clase Funcion
funcion = Funcion()

# Llamar a los métodos a través de la instancia creada

#Con esto consigo que en el servidor se imprima la fecha y hora actual en el servidor al inicio
#así puedo comprobar en el servidor que está bien, pero no es necesario
fecha_actual = funcion.obtener_fecha()
hora_actual = funcion.obtener_hora()

print("Fecha actual:", fecha_actual)
print("Hora actual:", hora_actual)
