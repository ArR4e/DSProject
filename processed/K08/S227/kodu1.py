from random import *
def bingo():
    tulemus = []
    for i in range(1):
        x = sample(range(1,10),3)
        tulemus+= x
    for i in range(1):
        t= sample(range(11,20),2)
        tulemus+= t
    
    return tulemus

