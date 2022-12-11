from random import *

def minu_shuffle(a):
    i = len(a)
    j = len(a)
    b = []
    while 0 < i:
        n = randint(0, j - 1)
        if n in b:
            while n in b:
                n = randint(0, j - 1)
        b += [n]
        a += [a[n]]
        del a[n]
        i -= 1