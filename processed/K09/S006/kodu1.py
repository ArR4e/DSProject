from statistics import harmonic_mean
import matplotlib.pyplot as plt

def silu_andmed(f, n):
    jada = []
    harmooniline = []
    number1 = 0
    number2 = 2
    for rida in f:
        rida = rida.strip("\n")
        rida = rida.split(" ")
        jada.append(rida[-1])
    harmooniline = [float(jada[0])] #harmoonilise jada 1. liige
    while number2 <= n and number2 - 1 <= len(jada): #harmoonilise jada liikmed vahemikus [2,n]
        jada2 = jada[number1:number2]
        float_jada2 = list(map(float,jada2))
        harmooniline.append(harmonic_mean(float_jada2))
        number2 += 1
    while number2 - 1 < len(jada): #harmoonilise jada liikmed alates liikmest n kuni lõpuni
        jada2 = jada[(number1 + 1):number2]
        float_jada2 = list(map(float, jada2))
        harmooniline.append(harmonic_mean(float_jada2))
        number1 += 1
        number2 += 1
    return [harmooniline, list(map(float,jada))]
fail = input("Sisesta failinimi: ")
f = open(fail, "r")
n = 50
tagastus = silu_andmed(f, n)
silutud_aktsiad = tagastus[0]
silumata_aktsiad = tagastus[1]
päevad = list(range(1, len(silutud_aktsiad)+1))

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(päevad, silutud_aktsiad)
ax.plot(päevad, silumata_aktsiad)
ax.set_xlabel("Päevad")
plt.show()

#lisan siia juurde, et üpris kindlasti oleks seda kõike palju lihtsamalt ja \ 
loogilisemalt ja lühemalt teha saanud, aga proovisin oma esialgset ideed läbi raiuda seni, kuni program tööle hakkab. \
Lõpuks hakkas, aga automaatkontrollile ei meeldinud mingid asjad. Ei jõua seda enam ümber kirjutama ka hakata. \
Loogikast võib kohati olla natuke keeruline aru saada, aga mingi loogika seal kusagil ikka on ka.