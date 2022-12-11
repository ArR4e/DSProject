from statistics import harmonic_mean
import matplotlib.pyplot as plt

f=open(input("Palun sisestage faili nimi: "))
read=f.readlines()
f.close()

andmed=[]
for i in range(len(read)):
    rida=read[i].split(",")
    arv=float(rida[1].strip().strip("\n"))
    andmed+=[arv]
silumata_andmed=andmed.copy()
    
def silu_andmed(j,n):
    a=[]
    silutud_andmed=[]
    i=1
    while i<n:
        silutud_andmed+=[harmonic_mean(j[0:i])]
        i+=1
    while len(j)>n:
        silutud_andmed+=[harmonic_mean(j[0:n])]
        j.pop(0)
    silutud_andmed+=[harmonic_mean(j[0:n])]
    return silutud_andmed

y1=silu_andmed(andmed,50)
y2=silumata_andmed
x=[]
for i in range(len(y1)):
    x+=[i+1]
 
fig = plt.figure()          
ax = fig.add_subplot(1,1,1)  

ax.plot(x,y1)
ax.plot(x,y2)
     

plt.show()                   

    