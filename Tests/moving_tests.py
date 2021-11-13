from puzzleclass import *
import numpy as np
import unittest

class TestMovingMethods(unittest.TestCase):
    def test_up(self):
        #  .fel() metodus tesztelese alapertelmezett parameterrel
        table = TologatosJatek(np.array([[6, 14, 10, 7], [5, 2, 0, 1], [15, 11, 3, 4], [12, 13, 8, 9]]))
        table.fel()
        calculated = table.A
        expected = np.array([[6, 14, 0, 7], [5, 2, 10, 1], [15, 11, 3, 4], [12, 13, 8, 9]])
        self.assertAlmostEqual(calculated.tolist(), expected.tolist())

    def test_down(self):
        #  .le() metodus tesztelese 1 parameterrel
        table = TologatosJatek(np.array([[6, 14, 10, 7], [5, 2, 0, 1], [15, 11, 3, 4], [12, 13, 8, 9]]))
        table.le(1)
        calculated = table.A
        expected = np.array([[6, 14, 10, 7], [5, 2, 3, 1], [15, 11, 0, 4], [12, 13, 8, 9]])
        self.assertAlmostEqual(calculated.tolist(), expected.tolist())

    def test_left(self):
        #  .balra() metodus tesztelese 2 parameterrel
        table = TologatosJatek(np.array([[6, 14, 10, 7], [5, 2, 0, 1], [15, 11, 3, 4], [12, 13, 8, 9]]))
        table.balra(2)
        calculated = table.A
        expected = np.array([[6, 14, 10, 7], [0, 5, 2, 1], [15, 11, 3, 4], [12, 13, 8, 9]])
        self.assertAlmostEqual(calculated.tolist(), expected.tolist())

    def test_right(self):
        #  .jobbra() metodus tesztelese
        table = TologatosJatek(np.array([[6, 14, 10, 7], [5, 2, 0, 1], [15, 11, 3, 4], [12, 13, 8, 9]]))
        table.jobbra()
        calculated = table.A
        expected = np.array([[6, 14, 10, 7], [5, 2, 1, 0], [15, 11, 3, 4], [12, 13, 8, 9]])
        self.assertAlmostEqual(calculated.tolist(), expected.tolist())

    def test_nullorder(self):
        #  .nullrendezes() metodus tesztelese
        table = TologatosJatek(np.array([[6, 14, 10, 7], [5, 2, 0, 1], [15, 11, 3, 4], [12, 13, 8, 9]]))
        table.nullrendezes()
        calculated = table.d[0]
        expected = [3, 3]
        self.assertAlmostEqual(calculated, expected)

if __name__ == '__main__':
    unittest.main()
