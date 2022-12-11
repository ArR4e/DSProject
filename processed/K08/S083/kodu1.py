from random import sample

def bingo():
    a = sample(range(1, 11), 3)
    if sum(a) == 6:
        return bingo()
    b = sample(range(11, 21), 2)
    järjend = a+b
    return järjend
    
