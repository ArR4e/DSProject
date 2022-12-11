import random
from random import sample

def bingo():
    arvud = []
    
    while True:
        arvud1 = sample(range(1, 11), 3)
        if arvud1.count(1) == 1 and arvud1.count(2) == 1 and arvud1.count(3) == 1:
            continue
        else:
            break
        
    for i in arvud1:
        arvud.append(i)
    
    arvud2 = sample(range(11, 21), 2)
    for i in arvud2:
        arvud.append(i)
    
    random.shuffle(arvud)
    
    return arvud
    
bingo()