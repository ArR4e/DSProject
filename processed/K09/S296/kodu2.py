import copy
from random import randint

def minu_shuffle(a):
    b = copy.deepcopy(a)
    for i in range(0,len(a)):
        c = randint(0,len(a)-1)
        a.append(a[c])
        a.pop(c)
    #return a
