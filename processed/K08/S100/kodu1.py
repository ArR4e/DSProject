from random import sample
def bingo():
    while True:
        alg = sample(range(1,11), 3)
        if sorted(alg) != [1, 2, 3]:
            break
    return alg + sample(range(11,21), 2)