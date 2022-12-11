from random import *
def bingo():
    jj=(sample(range(1,11),3))
    while 1 in jj and 2 in jj and 3 in jj:
        jj = sample(range(1,11),3)
    j = sample(range(11,21),2)
    jj.extend(j)
    return jj
bingo()
print(bingo())
        
    
    