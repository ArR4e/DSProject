from random import sample

def bingo():
    a = sample(range(1,11),3)
    numbrid = [1,2,3]
    if sum(a) == 6:
        a = sample(range(1,11),3)
        b = sample(range(11,21),2)
        return a + b
    else:
        b = sample(range(11,21),2)
        return a + b