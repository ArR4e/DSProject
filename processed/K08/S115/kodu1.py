from random import sample

def bingo():
    esimesed_kolm = sample(range(1,11), 3)
    teised = sample(range(11, 21), 2)
    if sum(esimesed_kolm) == 6:
        esimesed_kolm = sample(range(1,11), 3)
    arvud = esimesed_kolm + teised
    return arvud

print(bingo())        