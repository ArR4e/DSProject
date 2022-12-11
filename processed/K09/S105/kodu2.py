from random import randint

def minu_shuffle(a):
    if a!=[]:    
        b=[]
        for ele in a:
            b.append(ele)
        for i in range(0,len(a)-1):
            r=randint(0,len(b)-1)
            a[i]=b[r]
            b.pop(r)
        a[len(a)-1]=b[0]