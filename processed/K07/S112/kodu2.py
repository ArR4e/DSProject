
fail = open("taksohinnad.txt", encoding = "UTF-8")

pikkus = float(input("Sisesta tee pikkus kilomeetrites: "))

taksode_hinnad = []
nimed = []

for rida in fail:
    järjend = rida.split(",")
    nimi = järjend[0]
    alustus = float(järjend[1])
    kilomeeter = float(järjend[2].strip())
    
    pakutav_hind = alustus + kilomeeter*pikkus
    
    taksode_hinnad.append(pakutav_hind)
    nimed.append(nimi)

    
try:
    väikseim = min(taksode_hinnad)
    indeks = taksode_hinnad.index(väikseim)

    print(nimed[indeks])
    
except:
    print("-")
