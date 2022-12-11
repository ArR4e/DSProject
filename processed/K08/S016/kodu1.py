def bingo():
    j = []
    k = []
    e = sample(range(1,11), 3)
    for el in e:
        j += [el]
    f = sample(range(11, 21), 2)
    for ele in f:
        k += [ele]
    #return j, k
    kokku = sorted(j + k)
    lugeja = kokku.count(10)
    if kokku[0] == 1 and kokku [1] == 2 and kokku[2] == 3:
        return bingo()
    else:
        return kokku
        

from random import sample


print(bingo())
