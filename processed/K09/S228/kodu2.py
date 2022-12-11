from random import randint

def minu_shuffle(järjend):
    for i in range(len(järjend)):
        random_i = randint(0, len(järjend) - 1)
        järjend[i], järjend[random_i] = järjend [random_i], järjend[i]