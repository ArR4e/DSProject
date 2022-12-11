from statistics import harmonic_mean
import matplotlib.pyplot as plt

f = open(input("Sisestage faili nimi: "), "r+", encoding = "UTF-8")
lõpp_jär =[]
lõpp_jär2 = []
päevad = []
n = 0

maatriks = f.read().split("\n")
for andmed in maatriks:
    vajalik = andmed.split(",")[1]
    lõpp_jär.append(vajalik)
    n += 1
    päevad.append(n)

def silu_andmed(järjend, number):
    uus = list(map(float, järjend))
    for n in len(uus):
        uude = harmonic_mean(uus[n:(number+n)])
        lõpp_jär2.append(uude)
    return lõpp_jär2
        
fig = plt.figure()           # Kõigepealt loome joonist tähistava objekti
ax = fig.add_subplot(1,1,1)  # ja lisame joonisele joonestusala.
ax.set_ylim(0, 0.0175)         # Määrame y-telje nähtavuspiirkonna
ax.set_xticks([0,200,400,600,800,1000])  # ja x-telje märgid

ax.plot(päevad, lõpp_jär, "o-", label="Algandmed")
ax.plot(päevad, lõpp_jär2, "^-r", label="Silutud andmed")
ax.set_xlabel("Päevad")       # ja x-telje pealkirja

plt.show()           
        
        
    