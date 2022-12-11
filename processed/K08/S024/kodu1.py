from random import sample

järjend = []

def bingo():
    arvud_1 = sample(range(1,11),3)
    if sum(arvud_1) == 6:
        arvud_1 = sample(range(1,11),3)
    arvud_2 = sample(range(11,21),2)
    järjend = arvud_1 + arvud_2

    return järjend