from random import randint
def minu_shuffle(a):
    for i in a:
        b = randint(0,len(a)-1)
        c = a[b]
        x = randint(0,len(a)-1)
        y = a[x]
        a[b] = y
        a[x] = c
