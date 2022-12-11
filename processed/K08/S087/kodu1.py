from random import sample

def bingo():
    while True:
        a = sample(range(1,11), 3)
        b = sample(range(11,21), 2)
        c = [1,2,3]
        for el in a:
            if el in c:
                c.remove(el)
        koos = a + b
        if c != []:
            break
    return koos

