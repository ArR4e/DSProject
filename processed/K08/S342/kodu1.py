from random import sample
def bingo():
    esimesed = sample(range(1, 11), 3)
    while 1 in esimesed and 2 in esimesed and 3 in esimesed:
        esimesed = sample(range(1, 11), 3)
    teised = sample(range(11, 21), 2)
    väljund = esimesed + teised
    return väljund