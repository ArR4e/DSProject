from random import sample
from random import randint

def bingo():
    a = sample(range(1,11),3)
    if a[0] == 1 or a[0] == 2 or a[0] == 3:
        if a[1] == 1 or a[1] == 2 or a[1] == 3:
            if a[2] == 1 or a[2] == 2 or a[2] == 3:
                a[2] = randint(4,10)
    b = sample(range(11,21),2)
    return (a+b)
