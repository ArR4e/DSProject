from random import sample
def bingo():
    esimesed = sample(range(1, 11), 3)
    teised = sample(range(11, 21), 2)
    if (esimesed[0] == 1 and esimesed[1] == 2 and esimesed[2] == 3) or (esimesed[0] == 1 and esimesed[1] == 3 and esimesed[2] == 2) or (esimesed[0] == 2 and esimesed[1] == 3 and esimesed[2] == 1) or (esimesed[0] == 2 and esimesed[1] == 1 and esimesed[2] == 3) or (esimesed[0] == 3 and esimesed[1] == 2 and esimesed[2] == 1) or (esimesed[0] == 3 and esimesed[1] == 1 and esimesed[2] == 2):
            esimesed = sample(range(1, 11), 3)
    uus = esimesed + teised
    return uus
bingo()