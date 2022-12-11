from random import randint

def minu_shuffle(järjend):
    pikkus = len(järjend)
    if pikkus <= 1:
        print("Pole midagi segamini ajada")
    if pikkus > 1:
        for i in range(pikkus):
            arv = randint(0,pikkus-1)
            järjend[i],järjend[arv] = järjend[arv],järjend[i]