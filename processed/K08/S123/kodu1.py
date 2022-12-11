from random import sample

def bingo():
    osa1=sample(range(1,11),3)
    while 1 in osa1 and 2 in osa1 and 3 in osa1:
        osa1=sample(range (1,11),3)
    osa2=sample(range(11,21),2)
    
    return osa1+osa2

print(bingo())