teepikkus = float(input("Sisesta tee pikkus kilomeetrites: "))
fail = open("taksohinnad.txt", encoding="UTF-8")

taksode_hinnad = []
nimed = []

for rida in fail:
    element = rida.split(",")
    nimi = element[0]
    alghind = float(element[1])
    summa_1km = float(element[2])
    hind_km = alghind + summa_1km * teepikkus
    taksode_hinnad.append(hind_km)
    nimed.append(nimi)
    
odavaim = min(taksode_hinnad)
elemendi_nr = taksode_hinnad.index(odavaim)
odavaima_takso_nimi = nimed[elemendi_nr]

print("Kõige odavam on " + str(odavaima_takso_nimi))
            
fail.close()   