from random import randint
def minu_shuffle(a):
    n=len(a)
    for i in range(len(a)*3):
        x=randint(0,n-1)
        y=randint(0,n-1)
        z=a[x]
        a[x]=a[y]
        a[y]=z