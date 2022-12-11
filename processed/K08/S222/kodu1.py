from random import randint

def bingo():
    l = []
    n1 = randint(1,10)
    n2 = randint(1,10)
    n3 = randint(1,10)
    while n1 + n2 + n3 == 6 or n1 == n2 or n1 == n3 or n2 == n3:
        n1 = randint(1,10)
        n2 = randint(1,10)
        n3 = randint(1,10)
    n4 = randint(11,20)
    n5 = randint(11,20)
    while n4 == n5:
        n4 = randint(11,20)
        n5 = randint(11,20)
    return [n1,n2,n3,n4,n5]

print(bingo())