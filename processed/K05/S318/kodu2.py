import string
from random import *

def suurväike(x):
    pun=string.punctuation
    suv=str(pun[randint(0,len(pun)-1)])
    need=[]
    n=0
    for i in x:
        for i in pun:
            x=x.replace(i,suv)
    c=x.swapcase()
    return c
    