from random import sample

def bingo():
    x = []
    x += sample(range(1, 11), 3) + sample(range(11, 21), 2)

    while sum(x[0:3]) == 6:
        x += sample(range(1, 11), 3) + sample(range(11, 21), 2)
    return x

print(bingo())