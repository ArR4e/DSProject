import random
#a = [1, 3, 3, 4, 5, 5, 5, 6, 6]
def minu_shuffle(a):
    n=len(a)
    for i in range(n):
        j=random.randint(0, n-1)
        kustuta=a.pop(j)
        a.append(kustuta)
    #print(a)
#minu_shuffle([1, 3, 3, 4, 5, 5, 5, 6, 6])