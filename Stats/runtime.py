import time
from Stats.example_generator import *
from puzzleclass import TologatosJatek

"""
Ez a script egy rovid elemzest keszit a futasidokrol
"""

num_of_iters = 1000  # a statisztika ennyi darab pelda alapjan keszul

generate_start_time = time.time()
for _ in range(num_of_iters):
    generate_start_position()
generate_end_time = time.time()

print(str(num_of_iters), "db kezdőállás legenerálásához szükséges idő:",
      round(generate_end_time - generate_start_time, 5), "s")

games = [TologatosJatek(generate_start_position()) for _ in range(num_of_iters)]  # Letrehozom a lejatszando jatekokat
alg_start_time = time.time()
for game in games:
    game.kirakas()
alg_end_time = time.time()
del games  # kitoroljuk a TologatosJatek objektumokat, hogy nem foglaljak a memoriaban a helyet
print("Egy tábla kirakásának átlagos ideje", round((alg_end_time - alg_start_time) / num_of_iters, 5), "s")

shuffle_start_time = time.time()
for _ in range(num_of_iters):
    shuffle_position()  # Itt a default parameterek hasznaljuk, azaz 100 keveres a kirakott allason
shuffle_end_time = time.time()
print("Egy tábla összekevérese 100 lépéssel átlagosan",
      round((shuffle_end_time - shuffle_start_time) / num_of_iters, 5), "s időt vesz igénybe")
