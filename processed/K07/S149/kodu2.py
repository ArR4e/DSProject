f = open("taksohinnad.txt", encoding = "UTF-8")
hinnad = f.read().split("\n")
kaugus = float(input("Sisesta tee pikkus kilomeetrites: "))
nimi = []
soodsaim = []
try:
    for hind in range(len(hinnad)):
        hind = hinnad[hind].split(",")
        soodsaim += [float(hind[1]) + float(hind[2]) * kaugus]
        nimi += [hind[0]]
    print("Kõige odavam on", nimi[soodsaim.index(min(soodsaim))])
except:
    pass

f.close()