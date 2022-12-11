from random import randint
def minu_shuffle(jär):
    if jär!=[]:
        a=[]
        elemendid=jär[:]
        indeks=randint(0,len(jär)-1)
        for i in range(len(jär)):
            while indeks in a:
                indeks=randint(0,len(jär)-1)
            a.append(indeks)
        for i in range(len(jär)):
            jär[i]=elemendid[a[i]]