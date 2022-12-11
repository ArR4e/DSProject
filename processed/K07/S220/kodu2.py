pikkus = float(input("Sisesta tee pikkus kilomeetrites: "))

f = open("taksohinnad.txt", encoding="UTF-8")
taksod = {}
for i in f:
    nimi = i.split(",")[0]
    algus = float(i.split(",")[1])
    kilomeetrihind = float(i.split(",")[2])
    hind = algus + (pikkus * kilomeetrihind)
    taksod[nimi] = hind
    
f.close()
try:
    odavam = min(taksod.values())
    for i in taksod :
        if taksod[i] == odavam:
            print("kõige odavam on", i)
except :
    print("")

    

    
