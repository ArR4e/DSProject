from random import*
def bingo():
    while True:
        esimesedkolm=sample(range(1, 11), 3)
        viimasedkaks=sample(range(11,21), 2)
        if 1 in esimesedkolm and 2 in esimesedkolm and 3 in esimesedkolm:
            continue
        else:
            bingolist=esimesedkolm+viimasedkaks
            return bingolist
print(bingo())
