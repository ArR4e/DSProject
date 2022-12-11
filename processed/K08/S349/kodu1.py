from random import sample

def bingo():
    j1 = sample(range(1, 11), 3)
    j2 = sample(range(11, 21), 2)
    if sum(j1) == 6:
        return False
    else:
        järjestus = j1 + j2
        return järjestus

