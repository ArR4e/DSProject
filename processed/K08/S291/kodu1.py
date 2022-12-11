from random import sample

def bingo():
    while True:
        bingonumbrid = []
        bingonumbrid = bingonumbrid + sample(range(1, 11), 3) + sample(range(11, 21), 2)
        if 1 in bingonumbrid and 2 in bingonumbrid and 3 in bingonumbrid:
            continue
        else:
            return bingonumbrid