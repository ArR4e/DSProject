from random import sample

def bingo():
    x = sample(range(1, 11), 3)
    y = sample(range(11, 21), 2)
    
    while x == [1, 2, 3]:
        x = sample(range(1, 11), 3)
        
    bingonumbrid = x + y
    return bingonumbrid


        
    