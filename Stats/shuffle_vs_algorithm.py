import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from Stats.example_generator import *
from puzzleclass import TologatosJatek

"""
Ez a script egy matplotlib-es abrat keszit, ami a keveresek szama es a kirakakas lepesszama kozti osszefuggest abrazolja
Gyorsabb futas erdekeben a h-t novelni, a rep-et csokkenteni lehet,
de ezek valtoztatasaval nagyobb kilengesek tapasztalhatoak
"""

N = 1000  # maximum ennyi keverest csinalunk
h = 10  # x tengelyen a lepeskoz
rep = 20  # ennyi pelda alapjan szamolom az atlagot minden keveres szamnal
x = np.linspace(0, N, int(N / h + 1))
y = np.zeros_like(x)

for i in range(0, N + h, h):
    atlag_lepeszam = 0
    for _ in range(rep):
        table = shuffle_position(num_of_shuffles=i)
        game = TologatosJatek(table)
        game.kirakas()
        atlag_lepeszam += game.lepesekszama
    atlag_lepeszam = atlag_lepeszam / rep
    y[int(i / 10)] = atlag_lepeszam

fig, axs = plt.subplots(1, 1, figsize=(10, 10))
plt.plot(x, y)
plt.ylim(0, 500)
axs.set_title('Kirakás lépésszáma a keverések számának függvényében')
axs.set_ylabel('Kirakás lépésszáma')
axs.set_xlabel('Keverések száma')
plt.show()
