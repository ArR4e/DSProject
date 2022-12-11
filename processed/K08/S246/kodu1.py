from random import sample
def bingo():
    bingo_numbrid = []
    esimesed = sample(range(1, 11), 3)
    viimased = sample(range(11, 21), 2)
    while sum(esimesed) == 6:
        sample(range(1, 11), 3)
    bingo_numbrid = esimesed + viimased
    return bingo_numbrid