fail = open("taksohinnad.txt", encoding="UTF-8")
taksod = []
for rida in fail:
    taksod += rida.strip().split(",")
fail.close()

def odavaim_takso(teepikkus):
        hind = list(range(int(len(taksod)/3)))
        hind[0] = 0
        n = 0
        for i in range(0, len(taksod), 3):
            hind[n] = float(taksod[1+i]) + float(taksod[2+i])*teepikkus
            if n == 0:
                nimi = taksod[0+i]
                odavaim = hind[n]
            elif hind[n] < odavaim:
                nimi = taksod[0+i]
                odavaim = hind[n]
            n += 1
        valik = "Kõige odavam on " + nimi + "."
        return valik

sisend = float(input("Sisesta tee pikkus kilomeetrites: "))
if sisend == 0:
    pass
else:
    print(odavaim_takso(sisend))