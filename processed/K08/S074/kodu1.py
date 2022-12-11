#Import sample, et saada erinevad mittekorduvad arvud
from random import sample
#Bingo funktsaioon
def bingo():
    #2 erinevat tuhja listi kontrolliks, et numbrites ei esineks korraga 1,2,3
    bingo1 = []
    bingo2 = []
    #3 arvu vahemikus 1-10
    bingo1.extend(sample(range(1, 11), 3))
    if sum(bingo1) == 6:
        bingo1.clear()
        bingo1.extend(sample(range(1, 11), 3))
    #2 arvu vahemikus 11-20
    bingo2.extend(sample(range(11, 21), 2))
    #Listide kokku liitmine
    bingo3 = bingo1 + bingo2
    return bingo3
#Tulemuse valjastamine
print(bingo())
    