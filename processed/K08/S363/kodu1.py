def bingo():
    from random import sample
    numbrid = []
    esimesed = [1, 2, 3]
    while 1 in esimesed and 2 in esimesed and 3 in esimesed:
        esimesed = sample(range(1,11), 3)
        
    teised = sample(range(11,21), 2)
    
    for i in esimesed:
        numbrid.append(i)
        
    for i in teised:
        numbrid.append(i)
    
    return numbrid
