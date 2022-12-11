from random import *

def bingo():
    a = sample(range(1, 11), 3)
    
    while True:
        if a == [1,2,3] or a == [1,3,2] or a == [2,1,3] or a == [2,3,1] or a == [3,1,2] or a == [3,2,1]:
            a = sample(range(1, 10), 3)
        else:
            break
    
    a += sample(range(11, 21), 2)
    
    return a