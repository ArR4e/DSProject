from random import sample

def bingo():
    y = sample(range(11, 21), 2)
    x = sample(range(1, 11), 3)
    if x == [1, 2, 3]:
        x = sample(range(1, 11), 3)
    else:
        return(x+y)
bingo()