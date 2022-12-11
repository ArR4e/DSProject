import random

def minu_shuffle(l):
    for i in range(len(l)):
        r = random.randrange(i,len(l))
        l[i], l[r] = l[r], l[i]