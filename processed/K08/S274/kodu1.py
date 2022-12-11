from random import sample

def bingo():
    sõne1 = sample(range(1,11), 3)
    while True:
        if sum(sõne1) != 6:
            break
    sõne2 = sample(range(11, 21), 2)
    sõnekokku = sõne1 + sõne2
    return sõnekokku


