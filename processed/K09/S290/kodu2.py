from random import randint

def minu_shuffle(järjend):
    for i in range(0, len(järjend)-1):
        j = randint(0, i+1)
        järjend[i], järjend[j] = järjend[j], järjend[i]
