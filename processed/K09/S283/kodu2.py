from random import randint

def minu_shuffle(järjend):
    for vana in range(len(järjend) -1, 0, -1):
        uus = randint(0,vana)
        järjend[vana], järjend[uus] = järjend[uus], järjend[vana]

