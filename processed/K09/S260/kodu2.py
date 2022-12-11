from random import *

def minu_shuffle(l):
    for i in range(len(l)):
        r = randint(0,len(l)-1)
        l[0],l[r] = l[r],l[0]

minu_shuffle([5,3,6,5,5,3,4,1])
