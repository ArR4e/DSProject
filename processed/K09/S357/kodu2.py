from random import randint

def minu_shuffle(a):
    p = len(a) + 1
    for el in a:
        n = randint(0, p)
        a.pop(a.index(el))
        a.insert(n, el)