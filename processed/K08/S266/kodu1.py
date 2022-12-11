from random import sample

def bingo():
    eisobi = True
    while eisobi:
        numbrid = sample(range(1, 11), 3) + sample(range(11, 21), 2)
        eisobi = True if 3 in numbrid and 2 in numbrid and 1 in numbrid else False
        
    return numbrid

print(bingo())