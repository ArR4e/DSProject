
from random import *
a = [1, 3, 3, 4, 5, 5, 5, 6, 6]

def minu_shuffle(a):
    
    for x in range(0, 90): #for loop käib 90 korda läbi
        m = randint(0, len(a)-1)
        n = randint(0, len(a)-1)
        a[m], a[n] = a[n], a[m]
        
    return
