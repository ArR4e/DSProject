from random import sample

def bingo():
    esimesed=sample(range(1,11),3)
    if [1,2,3] in esimesed or [1,3,2] in esimesed or [2,3,1] in esimesed or [2,1,3] in esimesed or [3,1,2] in esimesed or [3,2,1]:
        esimesed=sample(range(1,11),3)
    teised=sample(range(11,21),2)
    summa=esimesed+teised
    return summa