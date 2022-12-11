tee_pikkus = float(input("Sisesta tee pikkus kilomeetrites: "))
f = open("taksohinnad.txt","r",encoding="utf-8")
odavaim_hind = -1
odavaim_takso = ''
for line in f:
    rida = line.rstrip()
    rida = rida.split(',')
    hind = float(rida[1])+tee_pikkus*float(rida[2])
    if hind < odavaim_hind or odavaim_hind == -1:
        odavaim_hind = hind
        odavaim_takso = rida[0]
f.close()
print("Kõige odavam on", odavaim_takso + '.')