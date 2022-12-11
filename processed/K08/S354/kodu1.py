from random import sample
def bingo():
    a = sample(range(1, 11), 3)
    while 1 and 2 and 3 in a:
        a = sample(range(1, 11), 3)
                
    b = sample(range(11, 21), 2)
    return a + b