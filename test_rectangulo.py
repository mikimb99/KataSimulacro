import unittest
import math
from rectangulo import Rectangulo
class Test_Rectangulo(unittest.TestCase):
#X1 X2 Y1 Y2 SON LOS VÉRTICES
    def test_area(self):
        rectangulo = Rectangulo(0,4,-2,2)
        self.assertEqual(rectangulo.calcular_area(), 8)
    def test_perimetro(self):

        rectangulo = Rectangulo(0, 4, -2, 2)
        self.assertEqual(rectangulo.calcular_perimetro(), 8)

    def test_centro(self):
        rectangulo = Rectangulo(0, 4, -2, 2)
        self.assertEqual(rectangulo.calcular_centro(), (2.0, 0.0))
    def test_diagonal(self):
        rectangulo = Rectangulo(0, 4, -2, 2)
        self.assertEqual(rectangulo.calcular_diagonal(), 4.47213595499958)



if __name__ == '__main__':
    unittest.main()