#FUNCIÓN PARA CONTAR LAS LETRAS A'S EN UN ARCHIVO

class Funcion:

    def count_a(self,file_path):
        count=0
        with open(file_path, 'r') as file:
            for line in file:
                count += line.count('a') + line.count('A')
            return count