from copy import copy
from random import randint
def minu_shuffle(a):
    c=copy(a)
    d=[]
    for i in range(len(c)):
        while True:
            b=randint(0,len(c)-1)
            if b not in d:
                break
        d.append(b)
        a[b]=c[i]
        