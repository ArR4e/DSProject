import random
def minu_shuffle(jada):
    maatriks=[]
    for el in jada:
        järg=random.random()
        maatriks.append([järg,el])
    maatriks.sort()
    for x in range(len(maatriks)):
        jada[x]=maatriks[x][1]
    #return jada