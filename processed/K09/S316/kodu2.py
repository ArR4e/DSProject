import random

def minu_shuffle(järjend):
    pikkus = len(järjend)
    for index, el in enumerate(järjend):
        juhuslik_indeks = random.randint(0,pikkus-1)
        järjend[juhuslik_indeks],järjend[index] = järjend[index],järjend[juhuslik_indeks]