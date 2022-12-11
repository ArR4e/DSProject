import random as r


def minu_shuffle(järjend):
    for i in range(len(järjend)):
        järjend.insert(r.randint(0,len(järjend)),järjend.pop(i))

a = [1, 3, 3, 4, 5, 5, 5, 6, 6]
minu_shuffle(a)

print(a)


    
        
        
    
    











