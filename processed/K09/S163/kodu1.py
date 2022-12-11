### Andmete silumine ###
import matplotlib.pyplot as plt

def silu_andmed(jär, n):
    x = 0
    silutud = []
    counter = 0
    pikkus = len(jär)
        
    for i in range(pikkus):
        if x < n:
            x += 1
            nimetaja = 0
            for j in range(x):
                nimetaja += (1/jär[j])            
            silutud.append(x/nimetaja)      
        
        if x == n:
            jär.pop(0)
            if len(jär) < n:
                break
            nimetaja = 0
            for k in range(x):
                nimetaja += (1/jär[k])
            silutud.append(x/nimetaja)
                             
    return silutud

print(silu_andmed([2, 1, 3, 4, 5], 3))

fail = open('aktsiad.txt')
andmed = []
päevad1 = []
päevad2 = []
x1 = 0
x2 = 0

for rida in fail:
    andmed.append(float(rida.split()[-1]))
  
andmed_oige = andmed.copy()
silutud = silu_andmed(andmed, 50)

for i in range(len(andmed_oige)):
    x1 += 1
    päevad1.append(x1)

for i in silutud:
    x2 += 1
    päevad2.append(x2)

plt.plot(päevad1, andmed_oige)
plt.plot(päevad2, silutud)

plt.show()

#print(len(päevad2))
#print(len(silutud))