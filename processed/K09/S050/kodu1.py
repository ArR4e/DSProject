def silu_andmed(hinnad,n):
    from statistics import harmonic_mean
    keskmistatud=[]
    loe=0
    for el in hinnad:
        if loe<=n-1:
            keskmistatud.append(float(harmonic_mean(hinnad[0:loe+1])))
            loe+=1
        else:
            keskmistatud.append(float(harmonic_mean(hinnad[loe+1-n:loe+1])))
            loe+=1
    return keskmistatud

f=open(input('Sisesta algandmete faili nimi: '),'r')
hinnajärjend=[]
for rida in f:
    rida=rida.split(', ')
    hinnajärjend.append(float(rida[1]))
    
print(silu_andmed(hinnajärjend,50))


import matplotlib.pyplot as plt

algandmed = hinnajärjend
silutud = silu_andmed(hinnajärjend,50)

fig = plt.figure()           
ax = fig.add_subplot(1,1,1)  

ax.plot(algandmed)  

ax.plot(silutud)

plt.show()                   