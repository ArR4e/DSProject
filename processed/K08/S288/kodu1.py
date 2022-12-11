from random import sample

def bingo():
    vahemik = []
    vahemik1 = sample(range(1, 11), 3)
    keelatud_numbrid = 1 in vahemik1 and 2 in vahemik1 and 3 in vahemik1
    if keelatud_numbrid == True:
        vahemik1 = sample(range(1, 11), 3)
    vahemik2 = sample(range(11, 21), 2)
    vahemik = vahemik1 + vahemik2
    return vahemik

print(bingo())