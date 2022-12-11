import random
def minu_shuffle(alist):
    for i in range(-1,(len(alist))-1,1):
        s = random.randint(0,len(alist)-1)
        alist[i], alist[s] = alist[s], alist[i]
    return