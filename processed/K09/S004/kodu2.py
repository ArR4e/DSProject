import random
def minu_shuffle(clist):
    for i in range(len(clist)):
        a=random.randint(0,len(clist)-1)
        b=clist[a]
        clist[a]=clist[i]
        clist[i]=b
    