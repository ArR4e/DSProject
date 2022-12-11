from random import sample
def bingo():
    s = sample(range(1, 11), 3)
    if sum(s) == 6:
        s = sample(range(1, 10), 3)
    return s + sample(range(11, 21), 2)
print(bingo())
