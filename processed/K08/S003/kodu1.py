def bingo():
    from random import sample
    numbrid = []
    numbrid.extend(sample(range(1,11),3))
    if 1 in numbrid and 2 in numbrid and 3 in numbrid:
       return bingo()
    numbrid.extend(sample(range(11,21),2))
    return numbrid