import random
from random import sample

def bingo():
    while True:
        vastus=[]
        arvud1=sample(range(1,11),3)
        for el in arvud1:
            vastus.append(el)
        arvud2=sample(range(11,21),2)
        for el in arvud2:
            vastus.append(el)
        vastus=sample(vastus,5)
        if 1 in vastus and 2 in vastus and 3 in vastus:
            continue
        else:
            break
    return vastus


