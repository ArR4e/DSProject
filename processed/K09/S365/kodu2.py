from random import *

alist = [1, 2, 3, 4, 5, 6, 7]

def minu_shuffle(alist):
    for i in range(0, len(alist)):
        x = alist.pop(i)
        y = randint(0, len(alist))
        alist.insert(y, x)

print(minu_shuffle(alist))