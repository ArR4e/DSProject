from random import randint

def minu_shuffle(a):
    if a == []:
        return
    else:
        for i in range(0,len(a)):
            n = randint(0,(len(a)-1))
            m = randint(0,(len(a)-1))
            b = a[n]
            a[n] = a[m]
            a[m] = b