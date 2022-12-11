from random import sample

def bingo():
    järjend=[]
    järjend+=sample(range(1, 11), 3)
    järjend+=sample(range(11,21),2)
    if sum(järjend[0:3])!=6:
        return järjend
    return bingo()
    
#print(bingo())