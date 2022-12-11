from random import *

def bingo():
    l = sample(range(1,11),3) + sample(range(11,21),2)
    if l.count(1) > 0 and l.count(2) > 0 and l.count(3) > 0:
        l = sample(range(1,11),3) + sample(range(11,21),2)
    return l 
    
bingo()