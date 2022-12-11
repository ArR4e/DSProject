import random

def minu_shuffle(a):
    for i in range(len(a)-1, 0, -1):
        suvaline = random.randint(0, i + 1)
        a[1], a[suvaline] = a[suvaline], a [i]