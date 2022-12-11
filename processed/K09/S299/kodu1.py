from statistics import harmonic_mean
import matplotlib.pyplot as plt

def silu_andmed(järjend,n):
    silutud=[]
    if n==1:
        silutud=järjend
    else:
        for arv in järjend:
           if n>järjend.index(arv):
               silutud= silutud+[harmonic_mean(järjend[0:järjend.index(arv)+1])]
           else:
               silutud= silutud + [harmonic_mean(järjend[järjend.index(arv)-(n-1):järjend.index(arv)+1])]
    return silutud

f=input('Sisestage faili nimi: ')
fail=open(f)
read=fail.readlines()
fail.close()
    
aktsiahinnad=[]
for el in read:
    el=el.strip('\n')
    el=el.split(', ')
    aktsiahinnad= aktsiahinnad + [float(el[1].strip())]
päevad=[]
i=0
while i < len(aktsiahinnad):
    päevad = päevad + [i+1]
    i+=1
    

fig = plt.figure()           
ax = fig.add_subplot(1,1,1)
ax.plot(päevad, silu_andmed(aktsiahinnad,50),label="silutud")
ax.plot(päevad,aktsiahinnad,label="silumata")
ax.set_xlabel("päevad")
ax.set_ylim(0, 0.018)         
ax.set_xticks([0,200,400,600,800,1000])
plt.show()

        
# tulemus on graafik kahe joonega, aga silutud andmetega joon ei ole nii ühtlane kui näites näha
# oli ning ma pole kindel, kuidas seda selliseks saada    
        