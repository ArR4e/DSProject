from random import randint
def minu_shuffle(a):
    n = len(a)
    for i in range(n):
        rand = randint(i, n-1)
        a[i], a[rand] = a[rand], a[i]
    
