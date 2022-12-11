from statistics import harmonic_mean
from urllib.request import urlopen
import matplotlib.pyplot as plt

#järjend aktsiate hindadest
failinimi = input("Sisesta faili nimi: ")
f = open(failinimi)

list_hinnad = []
while True:
    rida = f.readline()
    if rida == "":
        break
    else:
        rida2 = rida.strip("\n")
        rea_list = list(rida2.split(", "))
        hind = rea_list[-1]
        list_hinnad.append(hind)
f.close()


#silutud järjend aktsiate hindadest

def silu_andmed(järjend, n):
    kesk = []
    eelnevad_elemendid = [float(järjend[0])]
    for i in järjend[1:]:
        k = float(harmonic_mean(eelnevad_elemendid))
        kesk.append(k)
        if len(eelnevad_elemendid) < n:
            eelnevad_elemendid.append(float(i))
        else:
            eelnevad_elemendid.pop(0)
            eelnevad_elemendid.append(float(i))
    kesk.append(float(harmonic_mean(eelnevad_elemendid)))
    return kesk

a = silu_andmed(list_hinnad, 50)

päevad = list(range(0, len(a)))
#päevad2 = list(range(0, len(list_hinnad)))


#graafik
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(päevad, a)
#ax.plot(päevad2, list_hinnad)
plt.show()


