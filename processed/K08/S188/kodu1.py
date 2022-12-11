from random import *

def bingo():
    while True:
        tulemus = sample(range(1, 11), 3) + sample(range(11, 21), 2)
        if 1 in tulemus and 2 in tulemus and 3 in tulemus:
            continue
        else:
            return tulemus
    