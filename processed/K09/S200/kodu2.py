from random import randint

def minu_shuffle(järjend):
    pikkus1 = len(järjend)
    for i in range (0,pikkus1):
        pikkus = len(järjend)-1
        a = randint(0,pikkus)
        b = randint(0,pikkus)
        järjend[a], järjend[b] = järjend[b],järjend[a]
        
        
        