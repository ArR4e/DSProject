from random import sample

def bingo():
    kombinatsioon = []
    esimene = sample(range(1, 11), 3)
    while True:
        if 1 in esimene and 2 in esimene and 3 in esimene:
            esimene = sample(range(1, 11), 3)
        else:
            break
    kombinatsioon += esimene
    teine = sample(range(11, 21), 2)
    kombinatsioon += teine
    return(kombinatsioon)
