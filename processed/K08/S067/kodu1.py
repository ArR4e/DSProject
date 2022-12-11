from random import sample
def bingo():
    arvud = []
    a = sample(range(1, 11), 3)
    arvud = [i for i in a]
    b = sample(range(11, 21), 2)
    for i in b:
        arvud.append(i)
    if all(x in arvud for x in [2, 3, 1]):
        return bingo()
    else:
        return arvud

bingo()