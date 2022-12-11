from statistics import harmonic_mean
import matplotlib.pyplot as plt

jada=[]
def silu_andmed(failinimi, n):
    fail=open(failinimi, "r")
    for rida in fail:
        rida=rida.split(" ")
        arv=rida[-1]
        jada.append(float(arv))
    c=0
    keskmistatud=[]
    for i in jada:
        if c==0:
            keskm=jada[0]
        elif (c-n)<0:
            algus=0
            jada1=jada[algus:c]
            keskm=harmonic_mean(jada1)
        else:
            algus=((c-n)+1)
            jada1=jada[algus:c]
            keskm=harmonic_mean(jada1)
        keskmistatud+=[keskm]
        c=c+1
        
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.plot(jada, "b")
    ax.plot(keskmistatud, "r")
    plt.show()
    
silu_andmed("aktsiad.txt", 50)
