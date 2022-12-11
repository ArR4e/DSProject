from random import sample
def bingo():
    bingo = sample(range(1, 11), 3) + sample(range(11, 21), 2)
    return bingo
