from random import sample

def bingo():
    bingoNumbrid = []
    bingoNumbrid += sample(range(1,11), 3)
    bingoNumbrid += sample(range(11,21), 2)
    
    if 1 in bingoNumbrid and 2 in bingoNumbrid and 3 in bingoNumbrid:
        bingoNumbrid = bingo()
        
    return bingoNumbrid
        