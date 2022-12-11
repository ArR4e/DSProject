tee = float(input("Sisesta tee pikkus kilomeetrites: "))

def odav_takso(tee):
    f = open("taksohinnad.txt", encoding = "UTF-8")
    hind = 100000
    firma = "mitte miski"
    for rida in f:
        jupid = rida.split(",")
        uusfirma = jupid[0]
        sissehind = float(jupid[1])
        kilomhind = float(jupid[2])
        uushind = tee * kilomhind + sissehind
        if uushind < hind:
            hind = uushind
            firma = uusfirma
    f.close()
    print("Kõige odavam on " + str(firma) + ".")

odav_takso(tee)
