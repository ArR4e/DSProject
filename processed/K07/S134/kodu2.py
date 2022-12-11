teepikkus = float(input("Sisesta teepikkus kilomeetrites: "))
f = open("taksohinnad.txt")
taksode_hinnad = []
nimed = []
for rida in f:
    järjend = rida.split(",")
    a = järjend[1]
    b = järjend[2]
    nimi = järjend[0]
    hind = float(a) + teepikkus*float(b)
    taksode_hinnad.append(hind)
    nimed.append(nimi)
    väikseim = min(taksode_hinnad)
    indeks = taksode_hinnad.index(väikseim)
print("Kõige odavam on", nimed[indeks])
    

    
    
