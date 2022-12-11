

from random import *

def bingo():
    while True:
        üks = 0
        kaks = 0
        kolm = 0
        checker = 0
        esi3 = sample(range(1, 11), 3)
        if "1" in esi3:
            üks = 2
        if "2" in esi3:
            kaks = 2
        if "3" in esi3:
            kolm = 2
        checker = üks - kaks - kolm
        if (checker == -2):
            break
    vim2 = sample(range(11, 21), 2)
    
    bing = esi3 + vim2
    return bing

#print(bingo())

