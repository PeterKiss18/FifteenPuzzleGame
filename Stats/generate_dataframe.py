from puzzleclass import TologatosJatek
import pandas as pd
import numpy as np
import time
from Stats.example_generator import *

"""
This script generate 1000 games and save into a dataframe that contains data about the game
"""

df = pd.DataFrame(columns=('Kezdoallas', 'Lepesszam', 'Sikeres', 'Futasido (s)'))
num_of_rows = 1000

for i in range(num_of_rows):
    table = generate_start_position()  # generate a random start position
    start_position = table.reshape(16)
    game = TologatosJatek(table.copy())  # create a TologatosJatek object
    start_time = time.time()
    game.kirakas()  # solve the table
    runtime = round(time.time() - start_time, 5)
    num_of_steps = game.lepesekszama
    end_position = game.A.copy().reshape(16)
    expected_table = np.array(range(16))
    expected_table = np.roll(expected_table, -1)
    success = True if (end_position == expected_table).all() else False
    df.loc[i] = [start_position, num_of_steps, success, runtime]

df.to_csv('datas_for_stats.csv')
