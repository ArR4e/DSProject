def taksohind(tee):
    tuhh = []
    pikkus = float(tee)
    for i in taksod:
        nimi = i[0]
        sisse = float(i[1])
        teehind = float(i[2])
        tuhh.append(sisse + pikkus*teehind)
    try:
        best = min(tuhh)
        indekk = tuhh.index(best)
    except:
        print("taksot pole")
    if len(taksod) > 0:
        return indekk
    else:
        return "kaatkio"

        
f = open("taksohinnad.txt","r", encoding="UTF-8")

taksod = []

for i in f:
    rida = i.strip()
    rida1= rida.split(",")
    taksod.append(rida1)
    
teepikkus = float(input("sisesta tee pikkus: "))
if taksohind(teepikkus) == "kaatkio":
    print("taksot pole")
else:
    print("kõige odavam on sõita", taksod[taksohind(teepikkus)][0])

f.close()
