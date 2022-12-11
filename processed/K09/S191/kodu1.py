import matplotlib.pyplot as mpl
from statistics import harmonic_mean

def silu_andmed(sisse,n):
    last_n=[]
    keskmised=[]
    elemendid=[]
    x=0
    for el in sisse:
        elemendid+=[el]
        lugeja=0
        x+=1
        if type(el)==str:
            järjend=el.strip("\n").split(",")
            last_n.append(float(järjend[1]))
        elif type(el)==float or type(el)==int:
            last_n.append(el)
        if x<(n+1):
            for i in last_n:
                lugeja+=1/i
            keskmised+=[x/lugeja]
        else:
            last_n=last_n[1:]
            for i in last_n:
                lugeja+=1/i
            keskmised+=[n/lugeja]
    return keskmised
fail=input("Sisestage faili nimi: ")
list_len=[]
f=open(fail)
aktsiad=[]
indeksid=[]
indeks=0
for line in f:
    indeksid+=[indeks]
    indeks+=1
    aktsiad+=[float((line.strip("\n").split(","))[1])]
f.close()
#print(aktsiad,indeksid)
silutud=silu_andmed(aktsiad,50)
mpl.plot(indeksid,aktsiad)
#print(silutud)
mpl.plot(indeksid,silutud)
mpl.show()