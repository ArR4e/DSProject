from random import sample

def bingo():
    while True:
        järjend1=sample(range(1,11),3)
        järjend2=sample(range(11,21),2)
        järjend= järjend1+järjend2
        if 1 in järjend and 2 in järjend and 3 in järjend:
            continue
        else:
            break
    return järjend