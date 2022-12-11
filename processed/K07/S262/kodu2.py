f = open("taksohinnad.txt", encoding="UTF-8")
teepikkus = float(input("Sisesta tee pikkus kilomeetrites: "))
parimhind = 0
odavaim = ""
for rida in f:
    rida = rida.split(",")
    if float(rida[1]) + (float(rida[2]) * teepikkus) < parimhind or parimhind == 0:
        parimhind = float(rida[1]) + (float(rida[2]) * teepikkus)
        odavaim = rida[0]
print("Kõige odavam on", odavaim + ".")