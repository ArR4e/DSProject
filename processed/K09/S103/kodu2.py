from random import choice

def minu_shuffle(järjend):
    koopia = järjend.copy()
    for i in range(0,len(koopia)):
        valik = choice(koopia)
        järjend[i] = valik
        koopia.remove(valik)