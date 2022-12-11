from random import randint
def minu_shuffle(järjend):
    for n in range(len(järjend)):
        i = randint(0, len(järjend)-1)
        järjend[n], järjend[i] = järjend[i], järjend[n]