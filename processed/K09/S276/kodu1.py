from statistics import harmonic_mean
import matplotlib.pyplot as plt
fail=input("Sisesta faili nimi: ")
f=open(fail)
n=0
täpsus=int(input("Sisesta täpsus: "))
hinnad=[]
keskmised=[]
päevad=[]

def silu_andmed(hinnad, täpsus):
    if n < täpsus:
        keskmine=harmonic_mean(hinnad[0:n])
    else:
        keskmine=harmonic_mean(hinnad[n-50:n])
    return keskmine
           
for rida in f:
    järjend=rida.split(", ")
    hind=float(järjend[1].strip())
    hinnad.append(hind)
    n += 1
    päevad += [n]
    keskmised += [silu_andmed(hinnad, täpsus)]
f.close()

flg=plt.figure()
ax=flg.add_subplot(1,1,1)
ax.plot(päevad, hinnad)
ax.plot(päevad, keskmised)
ax.set_xlabel("Keskmised")        
plt.show()  