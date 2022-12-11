import random

def bingo():

    condition = True
    while(condition):
        x = random.sample(range(1, 11),3)

        if not (x[0] == 1):
            if not (x[1] == 2):
                if not (x[2] == 3):
                    if not(sum(x[0:4]) == 6):
                        y = random.sample(range(11,21),2)
                        x.extend(y)
                        return x
