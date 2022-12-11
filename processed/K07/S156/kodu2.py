

pikkus = float(input("Sisesta tee pikkus kilomeetrites: "))

taksod = []
with open("taksohinnad.txt", encoding="utf-8") as f:
    
    for i in f:
        taxi = i.replace("/n", ",").split(",")
        taksod.append((taxi[0], taxi[1], taxi[2]))
if taksod:
    hind = []
    for i in range(len(taksod)):
        hind.append(float(taksod[i][1]) + (float(taksod[i][2]) * pikkus))
    print("Kõige odavam on " + taksod[hind.index(min(hind))][0] + ".")