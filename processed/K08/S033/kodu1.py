import random

def bingo():
    ükskakskolm = [1, 2, 3]
    nr = random.sample(range(1, 11), 3)
    lisa = random.sample(range(11, 21), 2)
    nr = nr + lisa
    if ükskakskolm[0] in nr and ükskakskolm[1] in nr and ükskakskolm[2] in nr:
        nr = random.sample(range(1, 11), 3)
        lisa = random.sample(range(11, 21), 2)
        nr = nr + lisa
    return nr

print(bingo())