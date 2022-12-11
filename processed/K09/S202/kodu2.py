

import random

def minu_shuffle(a):
    copp = a.copy()
    leng = len(a)
    for i in range(0, leng):
        hmmm = random.choice(copp)
        a[i] = hmmm
        see = copp.index(hmmm)
        copp.pop(see)
    #return a
    
    
    
    
#print(minu_shuffle([1, 3, 3, 4, 5, 5, 5, 6, 6]))