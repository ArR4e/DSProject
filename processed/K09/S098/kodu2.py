from random import randint
b = [1, 2, 3, 4, 5, 6, 7]
g = []
def minu_shuffle(a):
    g = []
    while True:
        c = [randint(a[0], a[(len(a)-1)])]
        f = (randint(a[0], a[(len(a)-1)]))
        b.remove(f)
        g +=c
        if len(g) == len(b):
            break
        
    return g


print(minu_shuffle(b))