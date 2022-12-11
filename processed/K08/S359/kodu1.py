from random import sample


def bingo():
    while True:
        f=sample(range(1,11),3)
        f.sort()
        if f == [1,2,3]:
            continue
        else:
            break
    g=sample(range(11,21),2)
    arvud=f+g
    return arvud
bingo()