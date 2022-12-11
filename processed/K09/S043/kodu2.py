import random
tont = [1, 2, 3, 4, 5, 8, 14, 9, 2, 15]
def minu_shuffle(sisend = []):
    i = 0
    for el in sisend:
        lambine_indeks = random.randint(0, len(sisend)-1)
        uusl = sisend.pop(i)
        sisend.insert(lambine_indeks, uusl)
        i = i+1
    
print(minu_shuffle([1, 2, 3, 4, 5, 8, 14, 9, 2, 15]))
    
    