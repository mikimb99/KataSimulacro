import unittest
import math
class Test_Rectangulo(unittest.TestCase):
#X1 X2 Y1 Y2 SON LOS VÉRTICES
    def test_area(self):
        x1= 0
        x2= 4
        y1= -2
        y2= 2
        base= abs((x2-x1)) or abs(y2-y1)
        altura= abs((y1-x1)or (y2-x2))
        area = abs(base)* abs(altura)
        # CONDICIONES DE UN RECTÁNGULO
        if abs(y1-x1)==abs(y2-x2) and abs(x2-x1)==abs(y2-y1) and base!=altura:
            self.assertEqual((area), 8)
        else:
            raise ValueError('No es un rectángulo')
    def test_perimetro(self):
        x1 = 0
        x2 = 4
        y1 = -2
        y2 = 2
        base = abs((x2 - x1)) or abs(y2 - y1)
        altura = abs((y1 - x1) or (y2 - x2))
        perimetro= (abs(x1)+abs(x2)+abs(y1)+abs(y2))
        #CONDICIONES DE UN RECTÁNGULO
        if abs(y1 - x1) == abs(y2 - x2) and abs(x2 - x1) == abs(y2 - y1) and base != altura:
            self.assertEqual((perimetro), 8)
        else:
            raise ValueError('No es un rectángulo')

    def test_centro(self):
        x1 = 0
        x2 = 4
        y1 = -2
        y2 = 2
        base = abs((x2 - x1)) or abs(y2 - y1)
        altura = abs((y1 - x1) or (y2 - x2))
        centrox = (abs(x1) + abs(x2))/2
        centroy = (abs(y1) + abs(y2))/2
        centro= (centrox, centroy)
        # CONDICIONES DE UN RECTÁNGULO
        if abs(y1 - x1) == abs(y2 - x2) and abs(x2 - x1) == abs(y2 - y1) and base != altura:
            self.assertEqual((centro), (2.0,2.0))
        else:
            raise ValueError('No es un rectángulo')
    def test_diagonal(self):
        x1 = 0
        x2 = 4
        y1 = -2
        y2 = 2
        base = abs((x2 - x1)) or abs(y2 - y1)
        altura = abs((y1 - x1) or (y2 - x2))
        diagonal= math.sqrt(base**2+ altura**2)
        # CONDICIONES DE UN RECTÁNGULO
        if abs(y1 - x1) == abs(y2 - x2) and abs(x2 - x1) == abs(y2 - y1) and base != altura:
            self.assertEqual((diagonal), (4))
        else:
            raise ValueError('No es un rectángulo')



if __name__ == '__main__':
    unittest.main()