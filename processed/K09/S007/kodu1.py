from statistics import harmonic_mean
import matplotlib.pyplot as plt

f = input("Sisesta failinimi: ")
f = open(f, "r")
w =f.read()
w = w.strip()
w = w.split("\n")
kuupäevad = []
arvud =[]

for i in range(len(w)):
    w[i] = w[i].split(",")
    kuupäevad.append(w[i][0])
    arvud.append(float(w[i][1]))

f.close()

def silu_andmed(x,n):
    keskmistamine = []#järjend
    uus_järjend = []
    for i in range(len(x)):
        if len(keskmistamine) < n:
            keskmistamine.append(x[i])
        else:
            keskmistamine.pop(0)
            keskmistamine.append(x[i])  
        harmooniline = harmonic_mean(keskmistamine)
        uus_järjend.append(harmooniline)
    return uus_järjend
                
silutud = silu_andmed(arvud, 50)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)  
ax.plot(range(len(kuupäevad)), arvud)  
ax.plot(range(len(kuupäevad)), silutud)

plt.show() 
  
  
    
    
