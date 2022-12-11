from random import sample
def bingo():
    järjend = []
    while True:
        järjend += sample(range(1, 11), 3)
        järjend += sample(range(11, 21), 2)
        if 1 in järjend and 2 in järjend and 3 in järjend:
            järjend = []
            continue
        else:
            break
    return järjend