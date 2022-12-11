from math import *
pikkus=int(input('Sisestage elektriliini kogupikkus: '))
kaugus=int(input('Sisestage kahe posti vaheline maksimaalne kaugus: '))
arv=int(ceil(pikkus/kaugus))
if (arv-1)*kaugus < pikkus:
    arv+=1
print(arv)