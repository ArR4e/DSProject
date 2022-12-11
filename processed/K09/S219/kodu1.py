from statistics import harmonic_mean
import matplotlib.pyplot as plt

def silu_andmed(järjend, mitu_eelmist):
    uus = []   
    indeks = 0
    for arv in järjend:
        if indeks - mitu_eelmist >= 0:
            n_eelmist = järjend[indeks+1-mitu_eelmist:indeks+1]
            u = harmonic_mean(n_eelmist)
            uus.append(u)
        
        else:
            u = harmonic_mean(järjend[0:indeks+1])
            uus.append(u)
        indeks = indeks + 1
    print(uus)
    return uus


failinimi = input("Sisesta faili nimi: ")
with open(failinimi) as f:
    abilist = []
    for rida in f:
        ilma_reavahetuseta = rida.strip()
        praegune_rida = ilma_reavahetuseta.split(",")
        päeva_hind = float((praegune_rida[1]).lstrip())
        abilist.append(päeva_hind)

mitu_eelmist = int(input("Mitme elemendi kaupa keskmist rakendada: "))


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(abilist)
ax.plot(silu_andmed(abilist, mitu_eelmist))
plt.show()