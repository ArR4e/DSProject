from random import sample

def bingo():
    x = sample(range(1,11),3)
    y = sample(range(11,21),2)
    x = x + y
    z = 0
    for i in x:
        if i == 1 or i == 2 or i == 3:
            z+=1
            print(z)
            if z == 3:
                return bingo()
    return x

