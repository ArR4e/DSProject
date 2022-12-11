from random import sample
def bingo ():
    while True:
        a = []
        a = a + sample(range(1, 11), 3)
        a = a + sample(range(11, 21), 2)
        if 1 in a and 2 in a and 3 in a:
            continue
        else:
            break
    return (a)
print(bingo())