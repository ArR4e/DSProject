from random import randint

def minu_shuffle(järjend):
    n = len(järjend)
    a = randint(0, n)
    for el in järjend:
        järjend.insert(a,el)
    print (järjend)
        
    
    
minu_shuffle([1, 2, 3, 4, 5])
