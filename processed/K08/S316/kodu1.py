from random import sample

def bingo():
    arvud = []
    suvaline_arv = sample(range(1,11),3)
    suvaline_arv2 = sample(range(11,21),2)
    summa = sum(suvaline_arv)
    if summa == 6:
        suvaline_arv = sample(range(1,11),3)
    arvud = arvud + suvaline_arv[0:4] + suvaline_arv2[0:3]
    return arvud
    
