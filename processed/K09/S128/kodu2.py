#minu_shuffle
from random import *
def minu_shuffle(järjend):
    for i in range(0, len(järjend)):
        if i == len(järjend)-1:
            break
        else:
            koht = randint(i,len(järjend)-1)
            eemaldatud_el = järjend.pop(koht)
            järjend.append(järjend[i])
            järjend[i] = eemaldatud_el

"""sõne = input("Sisesta järjend: ") #[3, 4, 5, 6]
sõne = sõne[1:len(sõne)-1]
sisend = sõne.split(", ")
for i in range(0,len(sisend)):
    sisend[i] = int(sisend[i])"""
sisend = input()
minu_shuffle(sisend)
