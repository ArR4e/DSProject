import random

def minu_shuffle(a):
    pikkus = len(a)
    indeksid = random.sample(range(pikkus), pikkus)
    for i in range(pikkus):
        for j in indeksid:
            a[i], a[j] = a[j], a[i]