from random import randrange

def minu_shuffle(a):
    b=a.copy()
    i=0
    x=len(a)
    while i<x:
        del a[0]
        i+=1
    i=0
    while i<x:
        n=int(randrange(0,len(b)))
        a.append(b[n])
        del b[n]
        i+=1
a=[]