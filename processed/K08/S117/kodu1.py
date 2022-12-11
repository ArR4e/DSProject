#alustasin 15.10.2021 (22:10)
from random import sample

def bingo():
    while True:
        bingo1 = sample(range(1, 11), 3)
        bingo2 = sample(range(11, 21), 2)
        if sum(bingo1) != 6:
            return bingo1 + bingo2
            break