from random import sample
def bingo():
    a = list(sample(range(1, 11), 3)) + list(sample(range(11, 21), 2))
    if all(x in a for x in [1, 2, 3]):
        a = bingo()
    return a