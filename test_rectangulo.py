import unittest

class Test_Rectangulo(unittest.TestCase):

    def test_area(self):
        base= 5
        altura = 3
        area = base * altura
        self.assertEqual((area), 15)







if __name__ == '__main__':
    unittest.main()