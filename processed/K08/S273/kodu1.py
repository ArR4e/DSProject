from random import *

def bingo():
    while True:
        a = sample(range(1,11), 3)
        if a[0] == 1 or 2 or 3 and a[1] == 1 or 2 or 3 and a[2] == 1 or 2 or 3:
            continue
        b = sample(range(11,21), 2)
        break
    return a + b