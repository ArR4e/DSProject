from random import sample

def bingo():
    bingonumbrid = []
    
    bingonumbrid = bingonumbrid + sample(range(1, 11), 3)
    
    bingonumbrid = bingonumbrid + sample(range(11, 21), 2)
    
    if 1 in bingonumbrid and 2 in bingonumbrid and 3 in bingonumbrid:
        bingo()
    else:
        return bingonumbrid