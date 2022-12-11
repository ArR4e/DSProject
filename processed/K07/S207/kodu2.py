f = open("taksohinnad.txt", encoding = "UTF-8")
read = f.readlines()
f.close()

def hind(pikkus,alustus,hind):
    return pikkus*float(hind)+float(alustus)

pikkus = float(input("Sisestage taksosõidu pikkus: "))

parim_hind = 0
pakkuja = ""

for rida in read:
    ennik = rida.strip("\n").split(",")
    if parim_hind == 0:
        parim_hind = hind(pikkus, ennik[1], ennik[2])
        pakkuja = ennik[0]
    elif hind(pikkus, ennik[1], ennik[2]) < parim_hind:
        parim_hind = hind(pikkus, ennik[1], ennik[2])
        pakkuja = ennik[0]

print(f"Kõige odavam on {pakkuja}")