from random import randint

def minu_shuffle(järjend):
    for i in range(len(järjend)):
        tegur = randint(0, len(järjend) - 1)
        järjend[i], järjend[tegur] = järjend[tegur], järjend[i]
