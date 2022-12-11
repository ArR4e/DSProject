from random import sample

def bingo():
    bingo_nr = []
    esimesed = sample(range(1,11),3)
    while sorted(esimesed) == [1,2,3]:
        esimesed = sample(range(1,11),3)
    teised = sample(range(11,21),2)
    bingo_nr = bingo_nr + esimesed + teised
    return bingo_nr
  