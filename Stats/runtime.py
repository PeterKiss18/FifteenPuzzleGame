import time
from Stats.example_generator import *
from puzzleclass import TologatosJatek

num_of_iters = 1000

generate_start_time = time.time()
for _ in range(num_of_iters):
    generate_start_position()
generate_end_time = time.time()

print("1000 db kezdőállás legenerálásához szükséges idő:", round(generate_end_time-generate_start_time, 5), "s")

games = [TologatosJatek(generate_start_position()) for _ in range(num_of_iters)]
alg_start_time = time.time()
for game in games:
    game.kirakas()
alg_end_time = time.time()
del games
print("Egy tábla kirakásának átlagos ideje", round((alg_end_time-alg_start_time)/num_of_iters, 5), "s")

shuffle_start_time = time.time()
for _ in range(num_of_iters):
    shuffle_position()
shuffle_end_time = time.time()
print("Egy tábla összekevérese 100 lépéssel átlagosan", round((shuffle_end_time-shuffle_start_time)/num_of_iters, 5), "s időt vesz igénybe")
