from random import randint

def minu_shuffle(järjend):
    for element in järjend:
        indeks1 = randint(0,len(järjend)-1)
        indeks2 = randint(0,len(järjend)-1)
        järjend[indeks1],järjend[indeks2] = järjend[indeks2],järjend[indeks1]