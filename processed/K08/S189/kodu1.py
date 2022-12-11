from random import sample

def bingo():
    esimesed_kolm = sample(range(1,11),3)
    while sum(esimesed_kolm) == 6:
        esimesed_kolm = sample(range(1,11),3)
        continue
    teised_kaks = sample(range(11,21), 2)
    kokku = esimesed_kolm + teised_kaks
    return kokku

#bingo()