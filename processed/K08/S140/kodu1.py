from random import sample

def bingo():
    while True:
        a = sample(range(1, 11), 3)
        b = sample(range(11, 21), 2)
        c = a + b
        if 1 not in c or 2 not in c or 3 not in c:
            break
    return c
