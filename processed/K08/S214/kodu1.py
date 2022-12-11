from random import sample

def bingo():
    numbrid = []
    numbrid += sample(range(1,11),3)
    while True:
        if 1 in numbrid and 2 in numbrid and 3 in numbrid:
            numbrid = []
            numbrid +=sample(range(1,11),3)
        break
    numbrid += sample(range(11,21),2)
    return numbrid