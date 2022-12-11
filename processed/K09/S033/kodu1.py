from statistics import harmonic_mean

f = open("aktsiad.txt", encoding = "UTF-8")
hinnad = []
for rida in f:
    rida = rida.strip()
    rida = rida.split(', ')
    hinnad.append(float(rida[1]))
f.close()

def silu_andmed(järjend, n):
    keskmistatud = []
    
    jär = []
    for i in järjend[:n]:
        jär.append(i)  
        harm_kesk = harmonic_mean(jär)
        keskmistatud.append(harm_kesk)
        
    for i in järjend[n:]:
        jär.append(i)
        jär.pop(0)
        harm_kesk = harmonic_mean(jär)
        keskmistatud.append(harm_kesk)
    
    return keskmistatud

import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.plot(hinnad)
ax.plot(silu_andmed(hinnad, 50))

plt.show()