from random import sample

def bingo():
    while True:
        bingo_nr = sample(range(1, 11), 3) + sample(range(11, 21), 2)
        if [1, 2, 3] != sorted(bingo_nr)[0:3]:
            break
    return bingo_nr