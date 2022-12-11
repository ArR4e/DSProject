from random import sample

def minu_shuffle(j):
    n=len(j)
    järjekord=sample(range(0,n),n)
    jj=j.copy()
    for i in range(len(j)):
        j[i]=jj[järjekord[i]]

