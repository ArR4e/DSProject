import random

a = [10, 20, 30, 40]
def minu_shuffle(a):
    for i in a:
        arv = random.randint(0,len(a)-1)
        vahetus2 = a[arv]
        
        a[a.index(i)] = vahetus2
        a[arv] = i

minu_shuffle(a)