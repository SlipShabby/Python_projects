
import unittest
from logic import num_ind
from logic import init_grid

class Test_2048(unittest.TestCase):

    def test1(self):
        self.assertEqual(num_ind(1,2),7)

    def test2(self):
        self.assertEqual(num_ind(3,3),16)

    def test3(self):
        a =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        b = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]]
        self.assertEqual(init_grid(b),a)

    def test4(self):
        a =[ 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        b = [
            [1, 1, 1, 1],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]]
        self.assertEqual(init_grid(b),a)


    def test5(self):
        a =[]
        b = [
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1]]
        self.assertEqual(init_grid(b),a)

if __name__ == '__main__':
    unittest.main()