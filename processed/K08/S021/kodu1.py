from random import sample

def bingo():
    järjend1 = sample(range(1, 11), 3)
    if 1 in järjend1 and 2 in järjend1 and 3 in järjend1:
        return bingo()
    else:
        pass
    järjend2 = sample(range(11, 21), 2)
    järjend = järjend1 + järjend2
    return järjend

bingo()
    

    