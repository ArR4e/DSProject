from random import sample

def bingo():
    while True:
        arvud1 = sample(range(1, 11), 3)
        if all(i in arvud1 for i in [1,2,3]):
            continue
        break
    arvud2 = sample(range(11, 21), k=2)
    return arvud1 + arvud2