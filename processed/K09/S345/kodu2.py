from random import randint

def minu_shuffle(järjend):
    x = 0
    for i in range(len(järjend)):
        x = randint(0, len(järjend)-1)
        järjend[i], järjend[x] = järjend[x], järjend[i]
    print(järjend)