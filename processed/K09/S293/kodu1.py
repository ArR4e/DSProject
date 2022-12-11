from statistics import harmonic_mean
import matplotlib.pyplot as plt
nimi=input("Faili nimi: ")

f=open(nimi)
sisu=f.read()
sisu=sisu.replace("\n", ", ")
a=sisu.split(", ")
f.close()
e=[0]*(int(len(a)/2))
m=1
for i in range (int(len(a)/2)):
    e[i]=float(a[m]) #Hinnad
    m=m+2

päevad=[0]*(int(len(a)/2))
z=0
for i in range(int(len(a)/2)):
    päevad[i]=z
    z+=1


n=50
def silu_andmed(e,n):
    keskmistelist=[0]*(len(e))
    for i in range(len(e)):
        if i-n>=0:
            keskmistelist[i]+=harmonic_mean(e[i+1-n:i+1])
        else:
            keskmistelist[i]+=harmonic_mean(e[0:i+1])
    return(keskmistelist)
#print(silu_andmed(e,n))

    



#graafik
fig = plt.figure()
ax=fig.add_subplot(1,1,1)

#ax.plot(päevad, silu_andmed(e,n))
ax.plot(päevad, e)
ax.plot(päevad, silu_andmed(e,n))

ax.set_xlabel("Päevad")

ax.set_ylim(0, 0.0175)
ax.set_xticks([0,200,400,600,800,1000])
plt.show()