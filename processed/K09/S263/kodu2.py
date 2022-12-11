import random


def minu_shuffle(järjend):
    n = len(järjend)
    for i in range(n):
        suvaline_indeks = random.randint(0, n - 1)
        järjend[i], järjend[suvaline_indeks] = järjend[suvaline_indeks], järjend[i]

    #return järjend


järjend = [1, 2, 3, 4, 5, 6]
minu_shuffle(järjend)
#print(minu_shuffle(järjend))
