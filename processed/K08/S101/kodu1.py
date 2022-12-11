from random import *

def bingo():
    a=sample(range(1,11),3)
    b=sample(range(11,21),2)
    c=a+b
    while sorted(a)==[1,2,3]:
        a=sample(range(1,11),3)
        c=a+b
    return(c)
    
    
bingo()