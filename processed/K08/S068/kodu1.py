from random import sample

def bingo():
    numbrid=sample(range(1,11),3)
    numbrid=numbrid+sample(range(11,21),2)
    list(numbrid)
    
    return numbrid