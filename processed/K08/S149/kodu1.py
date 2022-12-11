from random import sample, randint

def bingo():
    while True:
        alla_10 =  sample(range(1, 11), 3)
        if sum(alla_10) > 6:
            break
    alla_20 = sample(range(11, 21), 2)
    return alla_10 + alla_20

bingo()