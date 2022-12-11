from random import randint
def minu_shuffle(järjend):
    n = len(järjend)
    i = 0
    for arv in range(n):
        suva = randint(arv, n-1)
        järjend[i], järjend[suva] = järjend[suva], järjend[i]
        i += 1
