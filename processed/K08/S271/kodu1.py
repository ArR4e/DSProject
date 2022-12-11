from random import sample

def bingo():
    while True:
        valik = sample(range(1,11), 3) + sample(range(11, 21), 2)
        if (1 in valik) == True and (2 in valik) == True and (3 in valik) == True:
            continue
        break   
    return  valik
