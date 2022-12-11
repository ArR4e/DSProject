from random import sample
def bingo():
    while True:
        x=0
        c=0
        y=0
        a=sample(range(1, 11), 3)+sample(range(11, 21), 2)
        for el in a:
            if el == 1:
                x=1
            if el == 2:
                c=1
            if el == 3:
                y=1
        if not (y==1 and x==1 and c==1):
            break
    return a