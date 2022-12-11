import matplotlib.pyplot as plt
from statistics import harmonic_mean

def silu_andmed(arg, n):
    harmonic = []
    for i in range(0, len(arg)):
        if i >= n:
            harmonic.append(harmonic_mean(arg[i-n+1:i+1]))
        else:
            harmonic.append(harmonic_mean(arg[0:i+1]))
    return harmonic

f_name = str(input("Sisestage failinimi: "))
f = open(f_name, encoding="UTF-8")
data = f.read().splitlines()
f.close()

original_data = []
harmonic_data = []
length = []
i = 0

for line in data:
    line = line.split(", ")
    original_data.append(float(line[1]))
    i += 1
    length.append(i)
    
harmonic_data = silu_andmed(original_data, 50)

fig = plt.figure()           # Kõigepealt loome joonist tähistava objekti
ax = fig.add_subplot(1,1,1)  # ja lisame joonisele joonestusala.

ax.plot(length, original_data)  # Lisame joonestusalale joondiagrammi
ax.plot(length, harmonic_data)
ax.set_xlabel("Aktsiad")        # ja x-telje pealkirja

plt.show()                   # Kuvame joonise ekraanile.