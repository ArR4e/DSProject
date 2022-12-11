from random import sample
import copy
def minu_shuffle(a):
    N = []
    pikkus = sample(range(0, len(a)), len(a))
    b = a.copy()
    for i in range(len(a)):
        a[i] = b[pikkus[i]]

a = [1, 3, 3, 4, 5, 5, 5, 6, 6]
minu_shuffle(a)
print(a)