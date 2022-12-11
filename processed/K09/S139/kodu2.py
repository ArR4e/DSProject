import random

def minu_shuffle(a):
    for i in range(0, len(a)-1):
        v = random.randint(0,len(a)-1)
        k = a[v]
        a[v] = a[i]
        a[i] = k
