import copy
import matplotlib.pyplot as plt

def silu_andmed(test, k):
    test2 = copy.deepcopy(test)
    for i in range(len(test)):
        if i < k-1:
            kesk = 0
            for p in range(i+1):
                kesk = kesk+1/test[p]       
            test2[i] = (i+1)/kesk
            #print(test2[i])
        if i >= k-1:
            kesk = 0
            e = i
            for p in range(k):
                kesk = kesk+1/test[e]
                e = e-1
            test2[i] = k/kesk
            #print(test2[i])
    return test2

fail = input("Siseta faili nimi: ")

#kuna n v22rtust ei olnud ylesande pystitamises mainitud, siis j2tan selle vaikimisi 50

f = open(fail)

aktsiad = []

for rida in f:
    rida = rida.strip().split(",")
    aktsiad.append(rida[1].strip())
f.close()

aktsiad = [float(i) for i in aktsiad]
aktsiad_silu = silu_andmed(aktsiad, 50)

arvud = []
for i in range(len(aktsiad)):
    arvud.append(i)               

fig = plt.figure()         
ax = fig.add_subplot(1,1,1)  
ax.plot(arvud, aktsiad)
ax.plot(arvud, aktsiad_silu) 
    
plt.show()                  