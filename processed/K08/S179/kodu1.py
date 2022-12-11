from random import sample

def bingo():
    arvud = []
    arvud = sample(range(1,11),3)
    while arvud[0]+arvud[1]+arvud[2] == 6:
        arvud = sample(range(1,4),3)
    arvud += sample(range(11,21),2)
    return arvud
    
    
print(bingo())
    