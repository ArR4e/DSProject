from random import sample
def bingo():
    esimesed_arvud = sample(range(1, 11), 3)
    summa = esimesed_arvud[0] + esimesed_arvud[1] + esimesed_arvud[2]
    teised_arvud = sample(range(11, 20), 2)
    if summa == 6:
        esimesed_arvud = sample(range(1, 11), 3)
        summa = esimesed_arvud[0] + esimesed_arvud[1] + esimesed_arvud[2]
        teised_arvud = sample(range(11, 20), 2)
        kõik_arvud = []
        return kõik_arvud + esimesed_arvud + teised_arvud
    else:
        kõik_arvud = []
        return kõik_arvud + esimesed_arvud + teised_arvud