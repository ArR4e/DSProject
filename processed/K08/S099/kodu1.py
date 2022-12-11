from random import sample

def bingo():
    j2r = []
    esimesed = sample(range(1, 11), 3)
    while 1 in esimesed and 2 in esimesed and 3 in esimesed:
        esimesed = sample(range(1, 11), 3)
    j2r += esimesed
    teised = sample(range(11, 21), 2)
    j2r += teised
    return j2r
    