f = open("taksohinnad.txt", encoding="UTF-8")

teepikkus = float(input("Sisestage tee pikkus (km): "))

nimed = []
hind_kokku = []

for rida in f:
    andmed = rida.split(",")
    
    nimi = andmed[0]
    nimed.append(nimi) #lisab saadud nime järjendisse
    
    sisseistumine = float(andmed[1])
    km_hind = float(andmed[2])
    
    läheb_maksma = sisseistumine + km_hind * teepikkus
    hind_kokku.append(läheb_maksma)

if hind_kokku == []:
    print(0)
else:
    odavaim = min(hind_kokku)
    odava_nimi = nimed[hind_kokku.index(odavaim)]

    print("Kõige odavam on " + odava_nimi + ".")

f.close()