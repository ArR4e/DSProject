from random import randint
import random

def minu_shuffle(järjend):
    uus = järjend[:]
    for i in range(5):
        index = random.randint(0, 5)
        temp = uus[i]
        uus1 = uus[index]
        uus[index] = temp
    return uus