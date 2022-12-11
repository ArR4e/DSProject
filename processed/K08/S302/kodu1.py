from random import sample
def bingo():
    sisu = []
    sisu = sample(range(1, 11),3) + sample(range(11,21),2)
    while sum(sisu[:3]) == 6:
        sisu = sample(range(1, 11),3) + sample(range(11,21),2)
        continue
    return sisu