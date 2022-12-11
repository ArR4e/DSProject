from random import sample

def bingo():
    järjend = sample(range(1,11), 3)
    järjend2 = sample(range(11, 21), 2)
    if järjend[0] == 1  and järjend[0] == 2 and järjend[0] == 3:
        järjend = sample(range(1,11), 3)
    järjend.extend(järjend2)
    return(järjend)



