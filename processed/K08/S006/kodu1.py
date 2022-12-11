from random import sample
import random

def bingo():
    kokku = []
    while True:
        numbrid = sample(range(1, 11), 3)
        if sum(numbrid) == 6:
            continue
        else:
            break
    arvud = sample(range(11, 21), 2)
    kokku = numbrid + arvud
    return(kokku)
print(bingo())