from random import sample

def bingo():
    numbrid=sample(range(1,11),3)
    numbrid.extend((sample(range(11,21),2)))
    return numbrid

print(bingo())
