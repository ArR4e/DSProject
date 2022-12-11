import random
def minu_shuffle(järjend):
    pikkus = len(järjend)
    
    for element in järjend:
        indeks = järjend.index(element)
        uus_indeks = random.randint(0,pikkus-1)
        järjend[indeks],järjend[uus_indeks]=järjend[uus_indeks],järjend[indeks]
        
       
    
järjend = [1, 3, 3, 4, 5, 5, 5, 6, 6]
print(minu_shuffle(järjend))