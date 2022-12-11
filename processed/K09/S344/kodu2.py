import random

a = [1, 2, 3, 4, 5, 6]

def minu_shuffle(x):
    pikkus = len(x)
    print(pikkus)
    for i in range(pikkus):
        juhuslik = random.randint(0, pikkus - 1)
        x[i], x[juhuslik] = x[juhuslik], x[i]
    print(str(x))

minu_shuffle(a)
    
