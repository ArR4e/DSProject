def bingo():
    from random import sample
    while True:
        numbrid = []
        numbrid = numbrid + sample(range(1,11),3)
        if 1 in numbrid and 2 in numbrid and 3 in numbrid:
            continue
        else:
            break
    numbrid = numbrid +sample(range(11,21),2)
        
    return numbrid
    