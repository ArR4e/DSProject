from random import sample

def bingo():
    numbrid = []
    kolm_nr = sample(range(1,11),3)
    kolm_nr.sort()
    if kolm_nr == [1,2,3]:
        kolm_nr = sample(range(1,11),3)
        numbrid.append(kolm_nr)
    kaks_nr = sample(range(11,21),2)
    bingo_nr = kolm_nr + kaks_nr
    return bingo_nr
    