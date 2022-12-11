# 1. Andmete silumine
# Ülesande link: https://courses.cs.ut.ee/2021/programmeerimine/fall/Main/Kodu9

# Tekstifailis aktsiad.txt on igal real kuupäev ning sellele kuupäevale vastav ühe ettevõtte aktsia hind.

# Kirjuta funktsioon silu_andmed, mis rakendab aktsia hindadele keskmistamist ning tagastab keskmistatud andmed
# uue järjendina. Keskmistamise all mõtleme siinkohal iga järjendi elemendi asendamist eelmise n elemendi
# aritmeetilise keskmisega. Funktsioon peab võtma argumendiks algandmed järjendina ning täisarvu, mis näitab,
# mitme elemendi kaupa keskmistamist rakendatakse.

# Näiteks järjendi [1, 3, 2, 4, 3, 5] puhul, kui n = 3, näeks arvutamine välja nii:

# [1/1, (1+3)/2, (1+3+2)/3, (3+2+4)/3, (2+4+3)/3, (4+3+5)/3] = [1, 2, 2, 3, 3, 4]
 #Näide funktsiooni käivitamisest:
# >>> silu_andmed([1, 3, 2, 4, 3, 5], 3)
#  [1.0, 2.0, 2.0, 3.0, 3.0, 4.0]
# Aritmeetilise keskmise leidmiseks soovitame kasutada Pythoni moodulis statistics asuvat funktsiooni mean:

# >>> from statistics import mean
# >>> mean([1, 2, 3, 2, 1])
# 1.8
# Seejärel kirjuta programm, mis kuvab nii algandmeid kui ka silutud andmeid graafikul.
# Graafikute joonistamiseks kasuta moodulit matplotlib, mille kohta saad rohkem lugeda siit.
# Tulemus võiks välja näha umbes selline (n = 50, algandmed siniselt, silutud punaselt):
from statistics import harmonic_mean
import matplotlib.pyplot as plt

def silu_andmed(järjend, n):
    järjend.reverse()
    avg2 = []
    for i in range(len(järjend)): 
        if i == len(järjend):
            avg2.append(järjend[i])
        else:
            avg = float(harmonic_mean(järjend[i:i+n]))
            avg2.append(avg)
    
    järjend.reverse() # ei tasu unustada järjendit tagasi pöörata! :)
    avg2.reverse()
    return avg2


# Faili avamine ja andmete sisselugemine
f = open("aktsiad.txt")
read = []
kuupäev = []
hind = []
for rida in f:
    r1 = rida.strip().split()
    read.append(r1)
    kuupäev.append(r1[0:3])
    hind.append(float(r1[3]))
f.close()

# silutud hinnad
silutud_hinnad = silu_andmed(hind, 50)

indeksid = [] # plottimise jaoks
for i in range(len(hind)):
    indeksid.append(i)

# Joonis
fig = plt.figure() # joonise objekt
ax = fig.add_subplot(1,1,1) # joonestusala
ax.plot(indeksid, hind) # joondiagramm
ax.plot(indeksid, silutud_hinnad) # joondiagramm
plt.show()

