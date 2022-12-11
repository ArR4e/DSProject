from random import *

def minu_shuffle(järjend):
    pikkus = len(järjend)
    while pikkus > 0:
        järjend += [järjend.pop(randint(0, pikkus - 1))]
        pikkus -= 1
