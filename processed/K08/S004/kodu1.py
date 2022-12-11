from random import sample
def bingo():
    y=[1,2,3]
    while y[0]+y[1]+y[2]==6:
        y=sample(range(1,11),3)
    a=sample(range(11,21),2)
    return(y+a)