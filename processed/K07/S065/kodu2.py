# 2. Takso hinnad

tee = float(input("Sisestage tee pikkus kilomeetrites: "))
fail = open("taksohinnad.txt", encoding ="UTF-8")

faili_sisu = []
kordus = 0

for rida in fail:
    faili_sisu.append(rida.strip().split(","))
    kordus = kordus + 1

fail.close()

a = 0
b = 0

nimed = []
hinnad = []

if faili_sisu != []:
    while kordus > 0:
        nimi = faili_sisu[a][b]
        hind = float(faili_sisu[a][b + 1]) + tee * float(faili_sisu[a][b + 2])
        nimed.append(nimi)
        hinnad.append(hind)
        a = a + 1
        kordus = kordus - 1
        
    odavaim = min(hinnad)
    indeks = hinnad.index(odavaim)
    print("Kõige odavam on ", nimed[indeks] + ".")
else:
    print(" ")