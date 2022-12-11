from random import *

def minu_shuffle(jarjend):
    indeksid = []
    pikkus = len(jarjend)
    for i in range(pikkus):
        indeksid.append(i)
    for i in range(pikkus):
       suvaline = choice(indeksid)
       jarjend.append(jarjend[suvaline])
       indeksid.remove(suvaline)
    for i in range(pikkus):
        del jarjend[0]

ls = [1, 3, 3, 4, 5, 5, 5, 6, 6]
minu_shuffle(ls)
print(ls)