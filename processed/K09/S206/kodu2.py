from random import choice

def minu_shuffle(a):
    b = a[:]
    for i in range(len(a)):
        k = choice(b)
        a[i] = k
        b.pop(b.index(k))
