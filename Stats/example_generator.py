from puzzleclass import TologatosJatek
import numpy as np
import random

def generate_start_position():
    elements = np.array(range(16))
    table = np.random.permutation(elements).reshape((4, 4))
    example = TologatosJatek(table)
    if example.megoldhatosag() == False:
        if table[3][3] != 0:
            table[3][3], table[3][2] = table[3][2], table[3][3]
        else:
            table[3][1], table[3][2] = table[3][2], table[3][1]
    return table

def shuffle_position(org_table = "Default", num_of_shuffles = 100):
    if type(org_table) == str:
        org_table = np.array(range(16))
        org_table = np.roll(org_table, -1)
        org_table.resize((4, 4))
    table = org_table.copy()
    game = TologatosJatek(table)
    directions = ["fel", "le", "jobb", "bal"]
    shuffle_count = 0
    while shuffle_count < num_of_shuffles:
        way = random.choice(directions)
        if way == "fel" and game.d[0][0] != 0:
            game.fel()
            shuffle_count += 1
        elif way == "le" and game.d[0][0] != 3:
            game.le()
            shuffle_count += 1
        elif way == "bal" and game.d[0][1] != 0:
            game.balra()
            shuffle_count += 1
        elif way == "jobb" and game.d[0][1] != 3:
            game.jobbra()
            shuffle_count += 1

    shuffled_table = game.A.copy()

    return shuffled_table
