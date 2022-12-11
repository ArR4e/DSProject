from random import randint
def minu_shuffle(a):
    b = len(a)
    x = 0
    while x <= b:
        a[x] = a[randint(0,b)]
        x += 1
    return (a)