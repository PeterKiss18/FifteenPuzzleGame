import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from Stats.example_generator import *
from puzzleclass import TologatosJatek

N = 1000
h = 10
rep = 20
x = np.linspace(0, N, int(N/h+1))
y = np.zeros_like(x)

for i in range(0, N+h, h):
    atlag_lepeszam = 0
    for _ in range(rep):
        table = shuffle_position(num_of_shuffles=i)
        game = TologatosJatek(table)
        game.kirakas()
        atlag_lepeszam += game.lepesekszama
    atlag_lepeszam = atlag_lepeszam/rep
    y[int(i/10)] = atlag_lepeszam


fig, axs = plt.subplots(1, 1, figsize=(10, 10))
plt.plot(x, y)
plt.ylim(0, 500)
plt.show()