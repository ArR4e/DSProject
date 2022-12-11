import random

k =[1,2,3,4,5,6,7]
def minu_shuffle(a):
    for x in range(len(a)-1,0,-1):#kasutasin Fisher-Yates algoritmi
        y = random.randint(0, x+1)
        a[x],a[y] = a[y],a[x]
        
    return a
    
print(minu_shuffle(k))

