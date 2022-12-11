from random import sample

def bingo():
    arvud = []
    arvud = arvud + list(sample(range(1, 11), 3))
    arvud = arvud + list(sample(range(11, 21), 2))
    if 1 in arvud:
        if 2 in arvud:
            if 3 in arvud:
                arvud = bingo()
    return arvud

print(bingo())


