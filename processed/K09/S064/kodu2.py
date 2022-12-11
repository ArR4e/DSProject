#2. minu_shuffle
from random import randint

def minu_shuffle(järjend):
    for el in range(len(järjend)):
        indeks = järjend[randint(0, el)]
        
        järjend.remove(indeks)
        järjend.insert(randint(0, el), indeks)
    print(järjend)
    
järjend = [1, 2, 3, 4, 5, 6]
minu_shuffle(järjend)