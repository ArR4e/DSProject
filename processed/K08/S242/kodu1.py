from random import sample

def bingo():
    kuni10 = sample(range(1, 11), 3)
    kuni20 = sample(range(11, 21), 2)
    if 1 in kuni10 and 2 in kuni10 and 3 in kuni10:
        kuni10 = sample(range(1, 11), 3)
    return kuni10 + kuni20
print(bingo())