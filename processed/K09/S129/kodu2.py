#minu_shuffle
from random import randint


def minu_shuffle(j):
    for i in range(1, len(j)):
        x = randint(0, len(j)-1)
        j[i], j[x] = j[x], j[i]
        