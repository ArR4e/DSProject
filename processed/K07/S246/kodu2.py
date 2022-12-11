fail = open('taksohinnad.txt', encoding = "utf-8")
teepikkus = float(input("Sisesta tee pikkus kilomeetrites: "))
def odavaim_takso():
    try:
        taksonimed = []
        takso_hinnad = []
        for rida in fail:
            nimekiri = rida.split(",")
            nimi = nimekiri[0]
            start_hind = float(nimekiri[1])
            km_hind = float(nimekiri[2])
            hind = start_hind + km_hind * teepikkus
            taksonimed.append(nimi)
            takso_hinnad.append(hind)
        vaikseim = min(takso_hinnad)
        indeks = takso_hinnad.index(vaikseim)
        print("Kõige odavam on " + taksonimed[indeks] + ".")
    except:
        print("Hinnakiri on tühi.")
    
odavaim_takso()
fail.close()