from random import sample

def bingo():   
    arvud=[]
    arvud_3 = sample(range(1,11),3)
    while sum(arvud_3) == 6:
        arvud_3 = sample(range(1,11),3)

    arvud_5 = sample(range(11,21),2)
    arvud=arvud_3+arvud_5
    return arvud

print(bingo())