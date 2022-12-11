from random import *
def bingo():
    while True:
        a=sample(range(1,11),3)
        if max(a)>3:
            break
    b=sample(range(11,21),2)
    c=a+b
    return(c)
