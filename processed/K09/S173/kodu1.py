from statistics import harmonic_mean
import matplotlib.pyplot as plt

def silu_andmed(järjend, n):
    x = 0
    muudetav = []
    for i in järjend:
        muudetav.append(järjend[x])
        if len(muudetav) > n:
            muudetav.pop(0)
        järjend[x] = float(harmonic_mean(muudetav))
        x += 1
    return(järjend)

faili_nimi = str(input("sisesta faili nimi:"))
fail = open(faili_nimi)

loe = 0
z = 0
aeg = []
hinnad = []
for i in fail.readlines():
    hind = ""
    for j in i:
        if j == ",":
            loe = 1
        elif loe == 1:
            hind += j
    loe = 0
    hind = hind.replace(",", "")
    hind = hind.replace("\n", "")
    hind = hind.replace(" ", "")
    hinnad.append(float(hind))
    aeg.append(z)
    z += 1
    
fig = plt.figure()           # Kõigepealt loome joonist tähistava objekti
ax = fig.add_subplot(1,1,1)  # ja lisame joonisele joonestusala.

ax.plot(aeg, hinnad, label="reaalne")
ax.plot(aeg, silu_andmed(hinnad, 50), label="silutud")# Lisame joonestusalale joondiagrammi
ax.set_xlabel("aeg")        # ja x-telje pealkirja
ax.legend()
plt.show()                   # Kuvame joonise ekraanile.z
    
fail.close()