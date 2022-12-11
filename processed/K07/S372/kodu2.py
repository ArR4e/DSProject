f = open("taksohinnad.txt", encoding="UTF-8")
pikkus = float(input("Sisesta tee pikkus kilomeetrites: "))
nimed = []
hinnad = []
for rida in f:
    realt = rida.strip().split(",")
    hind = float(realt[1]) + float(realt[2])*pikkus
    nimed.append(realt[0])
    hinnad.append(hind)

try:
    väikseim = min(hinnad)
    indeks = hinnad.index(väikseim)
    odavaim = (nimed[indeks])
    print("Kõige odavam on " + odavaim + ".")
except:
    print("")