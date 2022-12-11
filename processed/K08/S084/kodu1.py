from random import sample
def bingo():
    arvud = sample(range(1,11),3)
    while arvud.count(1)>0 and arvud.count(2)>0 and arvud.count(3)>0:
        arvud = sample(range(1,11),3)
    arvud += sample(range(11,21),2)
    return arvud
print(bingo())