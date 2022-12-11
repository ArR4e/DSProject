import random

def minu_shuffle(järjend):
    uus = []
    
    while len(järjend) > 0:
        indeks = random.randrange(0, len(järjend))
        uus.append(järjend.pop(indeks))
    järjend = uus