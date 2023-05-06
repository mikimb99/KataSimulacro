import unittest

class Test_Rectangulo(unittest.TestCase):

    def test_area(self):
        x1= 5
        x2 = 3
        y1= 5
        y2= 3
        area = abs(x1-x2)* abs(y1-y2)
        self.assertEqual((area), 4)







if __name__ == '__main__':
    unittest.main()