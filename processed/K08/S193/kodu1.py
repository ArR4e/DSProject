from random import sample
#5 arvu, millest 3 on vahemikus 1 kuni 10 ning ülejäänud 2 on vahemikus 11 kuni 20.

def bingo():
    esimene_vahemik = sample(range(1, 11), 3)
    teine_vahemik = sample(range(11, 21), 2)
    while 1 in esimene_vahemik and 2 in esimene_vahemik and 3 in esimene_vahemik:
        esimene_vahemik = sample(range(1, 11), 3)
    return esimene_vahemik + teine_vahemik

