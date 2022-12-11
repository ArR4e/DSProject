import random
def minu_shuffle(a):
    for y in range(len(a)):
        i = random.randint(y, len(a)-1)
        a[y], a[i] = a[i], a[y] 

    

        

    
    
    
    
a = [1, 3, 3, 4, 5, 5, 5, 6, 6]
minu_shuffle(a)