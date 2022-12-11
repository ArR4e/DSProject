from statistics import harmonic_mean
import matplotlib.pyplot as plt
########################################################################################################
### Failis aktsiad.txt on igal real kuupäev ning sellele vastav ühe ettevõtte aktsia hind.           ###
### Funktsioon silu_andmed rakendab aktsia hindadele keskmistamist ning tagastab keskmistatud andmed ###
### uue järjendina. Keskmistamine - iga järjendi elemendi asendamine eelmise n elemendi harmoonilise ###
### keskmisega. Kirjuta programm, mis kuvab nii algandmeid kui ka silutud andmeid graafikul.         ###                                                                                   ###
########################################################################################################
def silu_andmed(järjend, n):
    # kopeerime järjendi lokaalsesse muutujasse 'j'
    j = järjend[:]
    # tagastatav järjend keskmistatud andmetega 'uus_j'
    uus_j = []
    
    # iga järjendi elemendi indeksi järgi
    for i in range(len(j)):
        # kui eelmiseid elemente koos jooksva elemendiga on vähem kui 'n'
        # siis võtta nende elementide ((kaasaarvatud jooksev element)) harmoonilist keskmist
        if len(j[:i+1]) < n:
            # täiendame uue järjendise keskmistatud väärtusega
            uus_j.append(harmonic_mean(j[:i+1]))
        # kui eelmiseid elemente koos jooksva elemendiga on rohkem kui 'n'
        # siis võtta 'n' elemendist (kaasaarvatud jooksev element) harmoonilist keskmist
        else:
            # lisame uude järjendisse
            jada = list()
            for k in range(n-1, -1, -1):
                jada = jada + [j[i-k]]
            # lisame uude järjendisse
            uus_j.append(harmonic_mean(jada))
        #uus_j.append(h_m)
    return uus_j
########################################################################################################
faili_nimi = input('Sisestage aktsia hindade failinimi: ')
   
f = open(faili_nimi, 'r')
aktsiad = list()
for rida in f:
    rida = rida.split(',')
    aktsiad.append(float(rida[1].strip()))
f.close()

keskmistatud = silu_andmed(aktsiad, 50)
########################################################################################################
plt.title("Aktsia hindade keskmistamine")
plt.grid()
plt.plot(aktsiad, label='algandmed')
plt.plot(keskmistatud, label='silutud andmed')
plt.legend(loc='best')
plt.show()
########################################################################################################
