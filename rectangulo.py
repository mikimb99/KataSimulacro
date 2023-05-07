import math

class Noesrectangulo(Exception):
    print('No es un rectangulo')
class Rectangulo:
    def __init__(self, x1, x2, y1, y2):
        self.x1=  x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
    def comprobar_siesrectangulo(self):
        base = abs((self.x2 - self.x1)) or abs(self.y2 - self.y1)
        altura = abs((self.y1 - self.x1) or (self.y2 - self.x2))
        if abs(self.y1 - self.x1) == abs(self.y2 - self.x2) and abs(self.x2 - self.x1) == abs(
                self.y2 - self.y1) and base != altura:
            pass
        else:
            raise Noesrectangulo
    def calcular_centro(self):
        base = abs((self.x2 - self.x1)) or abs(self.y2 - self.y1)
        altura = abs((self.y1 - self.x1) or (self.y2 - self.x2))
        centro_x = (self.x1 + self.x2) / 2
        centro_y = (self.y1 + self.y2) / 2
        if abs(self.y1 - self.x1) == abs(self.y2 - self.x2) and abs(self.x2 - self.x1) == abs(
                self.y2 - self.y1) and base != altura:
            return (centro_x, centro_y)
        else:
            raise ValueError('No es un rectángulo')


    def calcular_perimetro(self):
        base = abs((self.x2 - self.x1)) or abs(self.y2 - self.y1)
        altura = abs((self.y1 - self.x1) or (self.y2 - self.x2))
        if abs(self.y1 - self.x1) == abs(self.y2 - self.x2) and abs(self.x2 - self.x1) == abs(
                self.y2 - self.y1) and base != altura:
            return abs(self.x1) + abs(self.x2) + abs(self.y1) + abs(self.y2)
        else:
            raise ValueError('No es un rectángulo')

    def calcular_area(self):
        base = abs((self.x2 - self.x1)) or abs(self.y2 - self.y1)
        altura = abs((self.y1 - self.x1) or (self.y2 - self.x2))
        if abs(self.y1 - self.x1) == abs(self.y2 - self.x2) and abs(self.x2 - self.x1) == abs(
                self.y2 - self.y1) and base != altura:
            return abs(base) * abs(altura)
        else:
            raise ValueError('No es un rectángulo')
    def calcular_diagonal(self):
        base = abs((self.x2 - self.x1)) or abs(self.y2 - self.y1)
        altura = abs((self.y1 - self.x1) or (self.y2 - self.x2))
        diagonal = math.sqrt(base ** 2 + altura ** 2)
        # CONDICIONES DE UN RECTÁNGULO
        if abs(self.y1 - self.x1) == abs(self.y2 - self.x2) and abs(self.x2 - self.x1) == abs(self.y2 - self.y1) and base != altura:
            return diagonal
        else:
            raise ValueError('No es un rectángulo')
