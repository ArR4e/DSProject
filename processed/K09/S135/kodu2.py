from random import randint

def minu_shuffle(j1):
    usedNr = j1[:]

    for i in range(len(j1)):
        nr = usedNr[randint(0, len(usedNr) - 1)]
        j1[i] = nr
        usedNr.remove(nr)