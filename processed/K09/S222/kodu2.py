from random import randint

def minu_shuffle(l):
    for _ in range(len(l)):
        n1 = randint(0,len(l)-1)
        n2 = randint(0,len(l)-1)
        while n1 == n2:
            n1 = randint(0,len(l)-1)
            n2 = randint(0,len(l)-1)
        l[n1],l[n2] = l[n2],l[n1]
    return l
