from random import randint


def minu_shuffle(järjend):
    for i in range(15):
        k = randint(0, len(järjend)-1)
        j = randint(0, len(järjend)-1)
        järjend[k], järjend[j] = järjend[j], järjend[k]
        

        
        
a = [1, 2, 3, 4, 5]
minu_shuffle(a)
print(a)
        
    

    

    

    
    