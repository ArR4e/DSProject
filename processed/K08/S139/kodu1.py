from random import sample
def bingo():
    permutatsioonid = [[3,2,1],[3,1,2],[2,3,1],[2,1,3],[1,2,3],[1,3,2]]
    esimesed = sample(range(1,10),3)
    teised = sample(range(11,21),2)
    if esimesed in permutatsioonid:
        esimesed = sample(range(1,11),3)
    return esimesed+teised
    
bingo()