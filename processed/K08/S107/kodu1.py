from random import sample

def bingo():
    järjend1 =  sample(range(1,11),3)
    järjend2 = sample(range(11,21),2)
    if 1 in järjend1 and 2 in järjend1 and 3 in järjend1:
        järjend1 = sample(range(1,11),3)
    return järjend1 + järjend2
