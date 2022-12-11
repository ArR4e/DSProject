# BINGO!

from random import sample

def bingo():
    while True:
        # Tekitan järjendi
        l1 = sample(range(1, 11), 3) + sample(range(11, 21), 2)
        if 1 in l1 and 2 in l1 and 3 in l1:
            continue
        else:
            break
    return l1

print(bingo())