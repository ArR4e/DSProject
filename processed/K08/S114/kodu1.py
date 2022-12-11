from random import sample

def bingo():
    arvud1 = sample(range(1,11),3)
    if sum(arvud1) == 6:
        while sum(arvud1) == 6:
            arvud1 = sample(range(1,11),3)
    arvud2 = sample(range(11,21),2)
    return arvud1+arvud2