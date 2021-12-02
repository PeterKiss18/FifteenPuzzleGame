import numpy as np
import unittest
from puzzleclass import TologatosJatek
from Stats.example_generator import generate_start_position

class MyTestCase(unittest.TestCase):
    def test_example(self):
        """
        Teszteli az algoritmust, hogy egy random megoldhato tablat kitud-e rakni
        """
        table = generate_start_position()
        game = TologatosJatek(table.copy())
        game.kirakas()
        solved_table = game.A.copy()
        expected_table = np.array(range(16))
        expected_table = np.roll(expected_table, -1)
        expected_table.resize(4, 4)
        self.assertTrue((solved_table == expected_table).all())

    def test_percentage_of_success(self):
        """
        Teszteli az algoritmus sikeresseget, hogy 100 megoldhato tablabol hanyat tud kirakni
        Hibat dob ha a kirakottak szama nem egyezik meg 100-al
        """
        success = 0
        num_of_interations = 100
        for _ in range(num_of_interations):
            table = generate_start_position()
            game = TologatosJatek(table.copy())
            game.kirakas()
            if game.megoldhatosag() == False: # Ebbe az agba jo esetben sose lep bele
                print(game.A)
            solved_table = game.A.copy()
            expected_table = np.array(range(16))
            expected_table = np.roll(expected_table, -1)
            expected_table.resize(4, 4)
            if (solved_table == expected_table).all():
                success += 1
            else:
                print(table.tolist())

        self.assertEqual(success, num_of_interations)

if __name__ == '__main__':
    unittest.main()
