#Minu shuffle
from random import randint

def minu_shuffle(järjend):
    if järjend == []:
        return
    for i in range(randint(1, 100)):
        a_indeks = randint(0, len(järjend) - 1)
        a = järjend[a_indeks]
        b_indeks = randint(0, len(järjend) - 1)
        b = järjend[b_indeks]
        järjend[a_indeks], järjend[b_indeks] = b, a


    