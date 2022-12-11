# 1. Bingo!

from random import sample

def bingo():
    while True:
        järjend1 = sample(range(1, 11), 3)
        if 1 not in järjend1 or 2 not in järjend1 or 3 not in järjend1:
            break
    järjend2 = sample(range(11, 21), 2)
    tulemusjärjend = järjend1 + järjend2
    return tulemusjärjend
    
tulemusjärjend = bingo()
print(str(tulemusjärjend))