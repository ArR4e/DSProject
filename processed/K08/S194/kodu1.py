from random import sample

def bingo():
    jarjend1  = sample(range(1, 11), 3)
    jarjend2  = sample(range(11, 21), 2)
    bongo = jarjend1 + jarjend2
    while 1 in bongo and 2 in bongo and 3 in bongo:
        jarjend1  = sample(range(1, 11), 3)
        jarjend2  = sample(range(11, 21), 2)
        bongo = jarjend1 + jarjend2
    return bongo
print(bingo())