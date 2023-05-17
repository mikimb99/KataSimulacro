import unittest
from funciones import Funcion

class Testcuenta_a(unittest.TestCase):
    def test_vacio(self):
        funcion = Funcion()
        file_path = 'test_file.txt'
        with open(file_path, 'w') as file:
            file.write('HI \n')
        count = funcion.count_a(file_path)
        self.assertEqual(count, 0)
    def test_aminuscula(self):
        funcion = Funcion()
        file_path = 'test_file.txt'
        with open(file_path, 'w') as file:
            file.write('aa \n')
        count = funcion.count_a(file_path)
        self.assertEqual(count, 2)
    def test_aMayus(self):
        funcion = Funcion()
        file_path = 'test_file.txt'
        with open(file_path, 'w') as file:
            file.write('AA \n')
        count = funcion.count_a(file_path)
        self.assertEqual(count, 2)
    def testlineas(self):
        funcion = Funcion()
        file_path = 'test_file.txt'
        with open(file_path, 'w') as file:
            file.write('AA \n')
            file.write('A       A \n')
            file.write('A13251346A \n')
        count = funcion.count_a(file_path)
        self.assertEqual(count, 6)
    def testmezcla(self):
        funcion = Funcion()
        file_path = 'test_file.txt'
        with open(file_path, 'w') as file:
            file.write('Aabonita  \n')
            file.write('a       eeepaA \n')
            file.write('a132a51346Aynueveson \n')
        count = funcion.count_a(file_path)
        self.assertEqual(count, 9)
if __name__ == 'main':
    unittest.main()