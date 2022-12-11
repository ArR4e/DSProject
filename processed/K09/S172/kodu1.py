from statistics import harmonic_mean
import matplotlib.pyplot as plt

def silu_andmed(hinnad, n):
    keskmised = []
    for i in range(0, len(hinnad)):
        if i-n>0:
            xyeta = hinnad[i-n+1:i]
            keskmised.append(harmonic_mean(xyeta))
        else:
            xyeta2 = hinnad[0:i+1]
            keskmised.append(harmonic_mean(xyeta2))
    return keskmised

f = open(input("Sisestage faili nimi: "))
kuupaevad = []
hinnad = []
for rida in f:
    rida = rida.strip()
    andmed = rida.split(',')
    kuupaevad += [andmed[0]]
    hinnad += [float(andmed[1])]
    
keskmised = silu_andmed(hinnad, 50)

f.close()

fig = plt.figure()           # Kõigepealt loome joonist tähistava objekti
ax = fig.add_subplot(1,1,1)  # ja lisame joonisele joonestusala.

ax.plot(kuupaevad, hinnad) 
ax.plot(kuupaevad, keskmised)  # Lisame joonestusalale joondiagrammi
ax.set_xlabel("Kuupäev")        # ja x-telje pealkirja

plt.show()                   # Kuvame joonise ekraanile.