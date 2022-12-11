from random import sample

def bingo():
    summa = 6
    järjend1 = []
    while summa == 6:
        esimene = sample(range(1, 11), 3)
        summa = sum(esimene)
        if summa !=6:
            järjend1 += esimene
        
    järjend2 = sample(range(11,21), 2)
    kokku = järjend1 + järjend2
    return kokku
