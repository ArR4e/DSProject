taksode_hinnad = []
nimed = []
f = open("taksohinnad.txt", "r", encoding="UTF-8")

kilomeeter = float(input("Sisesta tee pikkus kilomeetrites: "))

for rida in f:
    uus_rida = rida.strip("\n").split(",")
    nimi = uus_rida[0]
    stardi_hind = float(uus_rida[1])
    kilomeetri_hind = float(uus_rida[2])
    hind = stardi_hind + kilomeeter * kilomeetri_hind
    taksode_hinnad += [hind]
    nimed += [nimi]

try:
    indeks = taksode_hinnad.index(min(taksode_hinnad))
    odavaim_nimi = nimed[indeks]

except:
    odavaim_nimi = "puudu"
    
print("Kõige odavam on {}.".format(odavaim_nimi))

f.close()