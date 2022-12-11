from random import randint
def minu_shuffle(jarjend):
    indeks = 0
    for el in jarjend:
        a = jarjend.pop(indeks)
        b = randint(0, len(jarjend))
        jarjend.insert(b, a)
        indeks += 1
    print(jarjend)
    

    
    
    
    
    
    
    
    
    
    
    
    
    
minu_shuffle([1, 3, 5, 6])    
