from random import sample
def bingo():
    while True:
        bingonumbrid1kuni10 = sample(range(1, 11), 3)
        if bingonumbrid1kuni10 == [1, 2, 3]:
            continue
        elif bingonumbrid1kuni10 == [2, 3, 1]:
            continue
        elif bingonumbrid1kuni10 == [3, 1, 2]:
            continue
        elif bingonumbrid1kuni10 == [1, 3, 2]:
            continue
        elif bingonumbrid1kuni10 == [2, 1, 3]:
            continue
        elif bingonumbrid1kuni10 == [3, 2, 1]:
            continue
        else:
            bingonumbrid11kuni20 = sample(range(11, 21), 2)

        bingonumbrid = bingonumbrid1kuni10 + bingonumbrid11kuni20
        return bingonumbrid

bingo()