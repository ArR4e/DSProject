from statistics import harmonic_mean
import matplotlib.pyplot as plt

def silu_andmed(algandmed,n):
    andmed = []
    for i in range(len(algandmed)):
        if i < n:
            andmed.append(harmonic_mean(algandmed[0:i+1]))
        else:
            andmed.append(harmonic_mean(algandmed[i-n+1:i+1]))
    return andmed

f = open("aktsiad.txt","r")
text = f.read().splitlines()
f.close()

lines = sum(1 for line in text)

paevad = []
aktsia_hinnad = []

for i in range(lines):
    paevad.append(i)
    
for i in text:
    line = i.split(", ")
    aktsia_hinnad.append(line[1])
aktsia_hinnad = [float(i) for i in aktsia_hinnad]

plt.plot(paevad,aktsia_hinnad)
plt.plot(paevad,silu_andmed(aktsia_hinnad,50))
plt.xlabel("Päevad")

plt.show()