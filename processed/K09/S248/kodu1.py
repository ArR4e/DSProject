from statistics import harmonic_mean
import matplotlib.pyplot as plt

f=open(input("Sisesta faili nimi: "))
hinnad=[]
for i in f:
    hinnad.append(float(i.strip().split(", ")[1]))

f.close()   

def silu_andmed(x, y):
    ylist=[]
    m=[]
    for i in range(0,y):
            m.append(x[i])
            ylist.append(harmonic_mean(m))
            if i==len(x)-1:
                break
    n=1
    for i in range (0, len(x)-y):
        m=[]
        for i in range(n, n+y):
            m.append(x[i])
        ylist.append(harmonic_mean(m))
        n+=1
    return ylist
        
xlist=[]
for i in range(0,len(hinnad)):
    xlist.append(i)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.plot(xlist, hinnad)
ax.plot(xlist, silu_andmed(hinnad,50))

plt.show()







