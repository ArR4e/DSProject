import random

def minu_shuffle(järjend):
    for x in järjend:
        indeks = random.randint(0, len(järjend)-1)
        õige_indeks = järjend.index(x)
        järjend[indeks], järjend[õige_indeks]  = järjend[õige_indeks], järjend[indeks]



        