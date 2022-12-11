#bingo
from random import sample

def bingo():
    ühendlist = sample(range(1, 11), 3) + sample(range(11, 21), 2)
    while True:
        ü = ühendlist.copy()
        if ü[0] + ü[1] + ü[2] == 6:
            ühendlist = sample(range(1, 10), 3) + sample(range(11, 20), 2)
        ü = ühendlist.copy()
        if ü[0] + ü[1] + ü[2] != 6:
            break
    return ühendlist
