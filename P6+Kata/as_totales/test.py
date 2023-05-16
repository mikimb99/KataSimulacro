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

if __name__ == 'main':
    unittest.main()