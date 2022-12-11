from random import sample

def bingo():
    while True:
        bingonumbrid = []
        bingonumbrid += sample(range(1, 11), 3)
        if 1 in bingonumbrid and 2 in bingonumbrid and 3 in bingonumbrid:
            continue
        else:
            break
    bingonumbrid += sample(range(11, 21), 2)
    return bingonumbrid
