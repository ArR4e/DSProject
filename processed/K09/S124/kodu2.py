from random import sample, randint
import copy

def minu_shuffle(j):
    i = 0
    koopia = copy.deepcopy(j)
    indeksid = sample(range(0, len(j)), len(j))
    for indeks, element in zip(indeksid, j):
        j[i], koopia[indeks] = koopia[indeks], koopia[i]
        i += 1



  
    
    
    
#     pikkus = len(j)
#     indeksid = sample(range(0, (pikkus)), pikkus)
#     for el in indeksid:
#         j.index[el] = 
#     return j


#print(minu_shuffle([1, 3, 3, 4, 5, 5, 5, 6, 6]))
# pikkus = len(j)
# indeksid = sample(range(0, (pikkus)), pikkus)
# print(indeksid)
