from random import randint,sample
def bingo():
    bingolist = sample(range(1,11),3)
    while 1 in bingolist and 2 in bingolist and 3 in bingolist:
        bingolist = sample(range(1,11),3)
    bingolist.extend(sample(range(11,21),2))
    return bingolist