#FUNCIÓN PARA CONTAR LAS LETRAS A'S EN UN ARCHIVO

class Funcion:

    #Cuenta las a's totales del fichero
    def count_a(self,file_path):
        count=0
        with open(file_path, 'r') as file:
            for line in file:
                count += line.count('a') + line.count('A')
            return count
    #Cuenta las a's de cada línea
    def count_a_linea(self,file_path):
        line_count=0
        with open(file_path, 'r') as file:
            for line in file:
                count = line.count('a')+ line.count('A')
                line_count += 1
