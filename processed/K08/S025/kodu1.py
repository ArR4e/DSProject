from random import sample

def bingo():
    while True:
        a = sample(range(1, 11), 3)
        b = sample(range(11, 21), 2)
        järjend = a + b
        if 1 in järjend and 2 in järjend and 3 in järjend:
            continue
        else:
            return järjend