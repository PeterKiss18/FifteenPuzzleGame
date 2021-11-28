import unittest
from Stats.example_generator import generate_start_position
from puzzleclass import TologatosJatek

class TestExampleGenerator(unittest.TestCase):
    def test_solvable(self):
        # Test to the example generator give only solvable table
        num_of_iterations = 100
        for _ in range(num_of_iterations):
            tabla = generate_start_position()
            game = TologatosJatek(tabla)
            solvable = game.megoldhatosag()
            self.assertTrue(solvable)

if __name__ == '__main__':
    unittest.main()
