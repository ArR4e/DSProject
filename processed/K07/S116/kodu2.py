fail = open("taksohinnad.txt", "r", encoding="UTF-8")
teepikkus = float(input("Sisesta tee pikkus kilomeetrites: "))
odavaim = 999
odavfirma = ""
andmed = fail.readlines()

for line in andmed:
    rida = line.strip().split(",")
    hind = float(rida[1]) + float(rida[2]) * teepikkus
    if hind < odavaim:
        odavaim = hind
        odavfirma = rida[0]

print("Kõige odavam on " + odavfirma + ".")

fail.close()