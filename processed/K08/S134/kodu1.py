from random import sample

def bingo():
    while True:
        a = sample(range(1, 11), 3)
        if a == [1, 2, 3] or a ==[2, 3 , 1] or a ==[3, 2, 1] or a ==[1, 3, 2] or a ==[2, 1, 3] or a ==[3, 1, 2]:
            continue
        b = sample(range(11, 21), 2)
        c = a+b
        return(c)
bingo()