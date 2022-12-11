from random import*

def minu_shuffle(l):
    for i in l:
        suvaline = randint(0, len(l)-1)
        suvaline2 = randint(0, len(l)-1)
        l[suvaline], l[suvaline2] = l[suvaline2], l[suvaline]