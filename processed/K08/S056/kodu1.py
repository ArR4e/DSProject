from random import sample
def bingo():
    vahemik1 = sample(range(1, 11), 3)
    vahemik2 = sample(range(11, 21), 2)
    if sum(vahemik1) == 6:
        vahemik1 = sample(range(1, 11), 3)
        return vahemik1 + vahemik2
    else:
        return vahemik1 + vahemik2