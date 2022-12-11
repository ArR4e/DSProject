#Tekstifailis aktsiad.txt on igal real kuupäev ning sellele kuupäevale vastav ühe ettevõtte aktsia hind.
# Kirjuta funktsioon silu_andmed, mis rakendab aktsia hindadele keskmistamist ning tagastab keskmistatud andmed uue järjendina.
#Keskmistamise all mõtleme siinkohal iga järjendi elemendi asendamist eelmise n elemendi harmoonilise keskmisega.
#Funktsioon peab võtma argumendiks algandmed järjendina ning täisarvu, mis näitab, mitme elemendi kaupa keskmistamist rakendatakse.
#Harmoonilise keskmise leidmiseks soovitame kasutada Pythoni moodulis statistics asuvat funktsiooni ‘’harmonic_mean'':

# Seejärel kirjuta programm, mis kuvab nii algandmeid kui ka silutud andmeid graafikul. Graafikute joonistamiseks kasuta moodulit matplotlib,
#mille kohta saad rohkem lugeda siit. Tulemus võiks välja näha umbes selline (n = 50, algandmed siniselt, silutud punaselt):
#Vihje 1. Hoia funktsiooni sees järjendit viimase n elemendiga.

#Automaatkontroll. Funktsiooni nimi on silu_andmed ning tal on kaks parameetrit: ujukomaarvude järjend ja (positiivne) täisarv.
#Funktsioon tagastab ujukomaarvude järjendi. Algandmete faili nime küsida kasutajalt. Võib eeldada, et algandmete failis on päevade andmed eraldi ridadel.
#Iga päeva kohta on kirjas kuupäev ja selle päeva hind, eraldatult komaga. Read on järjestatud kuupäevade kasvamise järjekorras.
#Hind on mittenegatiivne ujukomaarv.
# from statistics import harmonic_mean
# file = input('Sisesta palun faili nimi:')
# opened_file = open(file, 'r')


# uus_järjend = []
# jagatav = 0
# def silu_andmed(järjend, n):
#     uus_järjend = []
#     suur_jagaja = 0
#     for i in range(len(järjend)):
#         jagaja = 1/järjend[i]
#         if (i + 1) > n:
#            suur_jagaja = suur_jagaja + jagaja
#            suur_jagaja = suur_jagaja - (1/järjend[(i-n)])
#         else:
#             suur_jagaja = suur_jagaja + jagaja
#         if (i + 1) > n:
#             väljund = n/suur_jagaja
#         else: 
#             väljund = (i +1)/suur_jagaja
#         uus_järjend = uus_järjend + [väljund]
#     return uus_järjend
# print(silu_andmed([2, 1, 3, 4, 5],3))
from statistics import harmonic_mean
import matplotlib.pyplot as plt

def silu_andmed(järjend, n):
    uus_järjend = []
    for indeks in range(1, len(järjend) + 1):
        algus = max(0, indeks - n)
        jagaja = harmonic_mean(järjend[algus:indeks])
        uus_järjend += [jagaja]
    return(uus_järjend)
# print(silu_andmed([2, 1, 3, 4, 5],3))
aktsiad = []
aktsiad2 = []
file = open((input('Sisesta palun faili nimi:')),"r")
# file = open('aktsiad.txt', 'r')
for data in file:
    data = data.strip()
    data = data.split()
    aktsiad = aktsiad + [float(data[3])]
file.close
täpselised_aktsiad = silu_andmed(aktsiad, 50)
plt.plot(aktsiad)
plt.plot(täpselised_aktsiad)
plt.xlabel("Aktsiate arv")
plt.ylabel("Aktsiad")
plt.show()


    



