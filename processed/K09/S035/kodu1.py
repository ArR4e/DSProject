def silu_andmed(järjend, arv):
    from statistics import harmonic_mean
    silutavad=[]
    silutud=[]
    for elem in järjend:
        silutavad.append(elem)
        if len(silutavad)==1:
            silutud.append(elem)
        elif arv==1:
            silutud.append(elem)
        elif len(silutavad)<arv:
            b=harmonic_mean(silutavad)
            silutud.append(b)
        elif len(silutavad)==arv:
            b=harmonic_mean(silutavad)
            silutud.append(b)
            silutavad.pop(0)
    return(silutud)

fail=str(input("Sisesta failinimi: "))
f=open(fail)
a=[]
for rida in f:
    rida2=rida.split(", ")
    a.append(float(rida2[1]))

import matplotlib.pyplot as plt
aeg=[]
for i in range(0, len(a)):
    aeg.append(i) 
fig = plt.figure()           
ax = fig.add_subplot(1,1,1)  
ax.plot(aeg, a)
ax.plot(aeg, silu_andmed(a, 50)) 
plt.show()                   
        
        
        