from random import sample
def bingo ():
    numbrid=[]
    esimesed=[1,2,3]
    while 1 in esimesed and 2 in esimesed and 3 in esimesed:
        esimesed=sample(range(1,11),3)
    teised=sample(range(11,21),2)
    for a in esimesed:
        numbrid.append(a)
    for a in teised:
        numbrid.append(a)
    return numbrid