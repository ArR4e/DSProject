from random import sample
def bingo():
    numbrid = sample(range(1,11),3)
    while sum(numbrid) == 6:
        numbrid = sample(range(1,11),3)
    numbrid += sample(range(11,21),2)
    return numbrid
