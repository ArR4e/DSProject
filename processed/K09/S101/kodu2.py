from random import randint
def minu_shuffle(x):
    n=0
    while n<len(x):
        nr=randint(0,len(x)-1)
        x[nr],x[n]=x[n],x[nr]
        n+=1