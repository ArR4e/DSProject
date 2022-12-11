tee_pikkus = float(input("Sisesta tee pikkus kilomeetrites: "))

fail = open("taksohinnad.txt", encoding = "UTF-8")

andmed = []
kordus = 0

for rida in fail:
    andmed.append(rida.strip().split(","))
    kordus += 1

fail.close()

i = 0
j = 0
nimed = []
hinnad = []

if andmed != []:
    while kordus > 0:
        nimi = andmed[i][j]
        hind = float(andmed[i][j + 1]) + tee_pikkus * float(andmed[i][j + 2])
        nimed.append(nimi)
        hinnad.append(hind)
        i += 1
        kordus -= 1
        
    väikseim = min(hinnad)
    indeks = hinnad.index(väikseim)
    print("Kõige odavam on", nimed[indeks] + ".")
else:
    print("Kõige odavamat taksofirmat ei ole, sest fail on tühi.")
