from random import sample

def bingo():
    järjend = []
    while True:
        järjend1 = sample(range(1, 11), 3)
        if 1 in järjend1 and 2 in järjend1 and 3 in järjend1:
            continue
        else:
            break
    järjend2 = sample(range(11, 21), 2)
    for el in järjend1:
        järjend.append(el)
    for el in järjend2:
        järjend.append(el)   
    return järjend