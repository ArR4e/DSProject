from random import sample

def bingo():
    lopp = []
    while True:
        lopp1 = sample(range(11,21),2)
        lopp2 = sample(range(1,11),3)
        for el in lopp2:
            lopp.append(el)
        for el in lopp1:
            lopp.append(el)
        if lopp[0:3] == 1 and lopp[0:3] == 2 and lopp[0:3] == 3:
            continue
        else:
            break
    return lopp    
