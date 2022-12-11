from random import sample

def bingo():
    a = sample(range(1, 11), 3)
    b = sample(range(11, 21), 2)
    if 1 in a and 2 in a and 3 in a:
        a = sample(range(1, 11), 3)
        return a+b
    else:
        return a+b

print(bingo())