from random import *

def minu_shuffle(järjend):
    for i in range(0, len(järjend)):
        j = randint(0, i)
        järjend[i], järjend[j] = järjend[j], järjend[i]
        
    print(järjend)
minu_shuffle([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
           