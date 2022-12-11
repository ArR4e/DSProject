from random import sample

def bingo():
    bingonumbrid1 = sample(range(1, 11), 3)
    while True:
        if 1 in bingonumbrid1 and 2 in bingonumbrid1 and 3 in bingonumbrid1:
            bingonumbrid1 = sample(range(1, 11), 3)
        else:
            break
    bingonumbrid2 = sample(range(11, 21), 2)
    return bingonumbrid1 + bingonumbrid2

print(bingo())