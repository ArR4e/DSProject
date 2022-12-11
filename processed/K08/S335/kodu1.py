from random import sample
def bingo():
    a = list(range(1, 11))
    b = list(range(11, 21))
    c = sample(a, 3)
    d = sample(b, 2)
    if 1 in c and 2 in c and 3 in c:
        c = sample(a, 3)
        return c + d
    else:
        return c + d