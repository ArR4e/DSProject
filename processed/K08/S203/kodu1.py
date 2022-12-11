from random import sample

def bingo():
    arvud = []
    kolm_arvu = sample(range(1, 11), 3)
    if sum(kolm_arvu) == 6:
        kolm_arvu = sample(range(1, 11), 3)
        arvud += kolm_arvu
    else:
        arvud += kolm_arvu
    viimased_kaks = sample(range(11, 21), 2)
    arvud += viimased_kaks
    return arvud

bingo()