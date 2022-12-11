tee = float(input("Sisesta tee pikkus kilomeetrites: "))

f = open("taksohinnad.txt", "r", encoding="UTF-8")

hind = []
nimi = []
for rida in f:
    rida = rida.strip().split(",")
    nimi.append(rida[0])
    hind.append(float(rida[1]) + float(rida[2]) * tee)
    
f.close()

try:
    odav = min(hind)
    print("Kõige odavam on", nimi[hind.index(odav)] + ".")
except:
    print("Antud fail on tühi.")
