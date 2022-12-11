from random import sample

def bingo():
    valmis = [1, 2, 3]
    while True:
        if 1 in valmis and 2 in valmis and 3 in valmis:
            esimene = sample(range(1, 11), 3)
            teine = sample(range(11, 21), 2)
            valmis = esimene+teine
        else:
            break
    return valmis