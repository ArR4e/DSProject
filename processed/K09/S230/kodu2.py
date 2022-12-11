from random import randint
def minu_shuffle(a):
    n=len(a)
    for i in range(n):
        arv=a[i]
        k=randint(0,n-1)
        a[i]=a[k]
        a[k]=arv