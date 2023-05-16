import math

class Noesrectangulo(Exception):
    print('No es un rectángulo')
    pass
class Rectangulo:
    def __init__(self, x1, x2, y1, y2):
        self.x1=  x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.comprobar_siesrectangulo()
    def comprobar_siesrectangulo(self):
        base = abs((self.x2 - self.x1)) or abs(self.y2 - self.y1)
        altura = abs((self.y1 - self.x1) or (self.y2 - self.x2))
        if abs(self.y1 - self.x1) == abs(self.y2 - self.x2) and abs(self.x2 - self.x1) == abs(
                self.y2 - self.y1) and base != altura:
            pass
        else:
            raise Noesrectangulo
    def calcular_centro(self):
        self.comprobar_siesrectangulo()
        centro_x = (self.x1 + self.x2) / 2
        centro_y = (self.y1 + self.y2) / 2
        return (centro_x, centro_y)


    def calcular_perimetro(self):
        self.comprobar_siesrectangulo()
        return abs(self.x1) + abs(self.x2) + abs(self.y1) + abs(self.y2)

    def calcular_area(self):
        self.comprobar_siesrectangulo()
        base = abs((self.x2 - self.x1)) or abs(self.y2 - self.y1)
        altura = abs((self.y1 - self.x1) or (self.y2 - self.x2))
        return abs(base) * abs(altura)

    def calcular_diagonal(self):
        base = abs((self.x2 - self.x1)) or abs(self.y2 - self.y1)
        altura = abs((self.y1 - self.x1) or (self.y2 - self.x2))
        diagonal = math.sqrt(base ** 2 + altura ** 2)
        return diagonal
