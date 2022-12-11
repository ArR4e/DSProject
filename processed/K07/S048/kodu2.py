tee_pikkus = float(input("Sisestage tee pikkus kilomeetrites: "))

f= open("taksohinnad.txt")
taksode_hinnad = []
nimed = []
for rida in f:
    üldinfo = rida.split(",")
    takso = üldinfo[0]
    stardihind = üldinfo[1]
    km_hind = üldinfo[2]
    hind = float(stardihind) + tee_pikkus*float(km_hind)
    taksode_hinnad.append(hind)
    nimed.append(takso)
miinimus = min(taksode_hinnad)
indeks = taksode_hinnad.index(miinimud)

print("Kõige odavam on", nimed[indeks] + ".")

f.close