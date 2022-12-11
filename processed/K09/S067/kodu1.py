from statistics import harmonic_mean as mean
from matplotlib import pyplot as plt
def silu_andmed(algandmed, kesk):
    uus = []
    i = 1
    while i <= kesk and len(uus) <= len(algandmed) - 1:
        uus.append(float(mean(algandmed[0:i])))
        i += 1
    while i <= len(algandmed) and len(uus) <= len(algandmed) - 1:
        uus.append(float(mean(algandmed[i-kesk:i])))
        i += 1      
    return uus

with open(input('Sisesta failinimi: '), encoding = 'UTF-8') as f:
    algandmed = []
    while True:
        g = f.readline().strip('\n')
        if g == '':
            break
        andmed = g.split(', ')
        algandmed.append(float(andmed[1]))
        
plt.plot(silu_andmed(algandmed, 50), 'b-', label = 'keskmistatud hind')
plt.title('Hinna graafik ajas', fontsize = 14)
plt.xlabel('Päevad', fontsize = 12)
plt.ylabel('Hind', fontsize = 12)
plt.plot(algandmed, 'r-', label = 'hind')
plt.legend()
plt.show()