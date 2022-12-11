from random import sample

def bingo():
    järjend = sample(range(1, 11), 3)
    järjend += sample(range(11, 21), 2)
    
    while True:
        if 1 in järjend and 2 in järjend and 3 in järjend:
            järjend = sample(range(1, 10), 3)
            järjend += sample(range(11, 21), 2)
        else:
            return järjend
            break