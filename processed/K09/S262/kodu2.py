from random import randint
def minu_shuffle(sisend):
    arvud = len(sisend)
    while arvud > 0:
        n = randint(0,arvud-1)
        a = sisend[n]
        sisend.append(sisend.pop(n))
        arvud -= 1