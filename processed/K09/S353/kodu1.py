from statistics import harmonic_mean
import matplotlib.pyplot as plt
def silu_andmed(järjend, n):
    tulemus=[]
    n2=1
    for i in range(len(järjend)):
        if n2<=n:
            tulemus.append(float(harmonic_mean(järjend[:i+1])))
        else:
            tulemus.append(float(harmonic_mean(järjend[i-n+1:i+1])))
        n2+=1
    return tulemus
print(silu_andmed([2, 1, 3, 4, 5], 3))
sisend=input('Palun sisestage faili nimi: ')
kuupäevajärjend=[]
arvudejärjend=[]
with open(sisend) as fail:
    for rida in fail:
        i=rida.find(',')
        kuupäevajärjend.append(rida[:i].strip())
        arvudejärjend.append(float(rida[i+1:].strip()))
päevadejärjend=range(len(kuupäevajärjend))
fig=plt.figure()
ax=fig.add_subplot(1,1,1)
ax.plot(päevadejärjend, arvudejärjend)
ax.plot(päevadejärjend, silu_andmed(arvudejärjend, 50))
ax.set_xlabel('Päevad')
ax.set_ylabel('Hind')
plt.show()