from random import *

def bingo():
    esimesed3 = sample(range(1, 11), 3)
    while sum(esimesed3) == 6:
       esimesed3 = sample(range(1, 11), 3) 
    viimased2 = sample(range(11, 21), 2)
    return esimesed3 + viimased2

print(bingo())