from random import*
def bingo():
    nr=[1,2,3]
    while 1 in nr and 2 in nr and 3 in nr:
        nr=sample(range(1,11),3)
        nr+=sample(range(11,21),2)
    return nr
print(bingo())