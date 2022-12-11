kilomeetrid = float(input("Sisesta tee pikkus kilomeetrites: "))
if kilomeetrid <= 0:
    raise Exception("Valed andmed!")

fail = open("taksohinnad.txt", encoding="UTF-8")
hinnad = []
nimed = []
for rida in fail:
    nimi, stardihind, km = rida.strip().split(",")
    taksohind = kilomeetrid * float(km) + float(stardihind)
    nimed = nimed + [nimi]
    hinnad = hinnad + [taksohind]
    odavaim = min(hinnad)
    indeks = hinnad.index(min(hinnad))
    takso = nimed[indeks]
    
print("Kõige odavam on " + takso + ".")

fail.close()
    