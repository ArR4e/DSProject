from random import sample

def minu_shuffle(a):
    varua=a.copy()
    pikkus=len(a)
    x=sample(range(0,pikkus), pikkus)
    for i in range(pikkus):
       
        a[i]= varua[x.pop(0)]
        x.append(0)
        
