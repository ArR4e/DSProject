import copy
import random
def minu_shuffle(a):
    koopia = copy.copy(a)
    s = 1
    for el in range(0,len(a)):
        index = random.randint(0,len(a)-s)
        a[el] = koopia[index]
        del koopia[index]
        s += 1
    return a

print(minu_shuffle([1,2,3,4,5,6,7,8,9]))