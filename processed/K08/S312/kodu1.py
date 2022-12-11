from random import sample

def bingo():
    while True:
        a = sample(range(1, 11), 3)
        b = sample(range(11, 21), 2)
        c = a + b
        if 1 in c and 2 in c and 3 in c:
            continue
        else:
            return c
            break
