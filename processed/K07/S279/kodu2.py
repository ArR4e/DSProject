tee_pikkus = float(input("Sisesta tee pikkus kilomeetrites: "))

fail = open("taksohinnad.txt", encoding="UTF-8")

taksode_hinnad = []
taksode_nimed = []

for rida in fail:
    järjend = rida.split(',')
    takso = järjend[0]
    stardihind = järjend[1]
    km_hind = järjend[2]
    maksumus = float(stardihind) + tee_pikkus*float(km_hind)
    taksode_hinnad.append(maksumus)
    taksode_nimed.append(takso)
    
try:
    väikseim = min(taksode_hinnad)
    indeks = taksode_hinnad.index(väikseim)
    odavaim_takso = taksode_nimed[indeks]
    print("Kõige odavam on " + odavaim_takso + "." )
except:
    print("Midagi on valesti.")

fail.close()