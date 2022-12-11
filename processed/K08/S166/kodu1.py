from random import sample

def bingo():
    while True:
        x=sample(range(1,11),3)+sample(range(11,21),2)
        if 1 in x and 2 in x and 3 in x:
            continue
        else:
            break
    return x
