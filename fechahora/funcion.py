import time

class Funcion:
    def obtener_fecha(self):
        return time.strftime("%Y-%m-%d", time.gmtime())

    def obtener_hora(self):
        return time.strftime("%H:%M:%S", time.gmtime())

# Crear una instancia de la clase Funcion
funcion = Funcion()

# Llamar a los métodos a través de la instancia creada
fecha_actual = funcion.obtener_fecha()
hora_actual = funcion.obtener_hora()

print("Fecha actual:", fecha_actual)
print("Hora actual:", hora_actual)
