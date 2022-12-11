from random import sample

def bingo():
    numbrid = sample(range(1, 11), 3) + sample(range(11, 21), 2)
    while 1 in numbrid and 2 in numbrid and 3 in numbrid:
        numbrid = sample(range(1, 11), 3) + sample(range(11, 21), 2)
    return numbrid

#print(bingo())