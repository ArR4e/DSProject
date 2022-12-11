file = open("taksohinnad.txt", "r", encoding="utf-8")
filesisu = file.readlines()
s = float(input("Sisesta tee pikkus kilomeetrites: "))
kokkufirma = 999999
odavaim = "FAIL ON TÜHI"
for rida in filesisu:
    sõne = rida.strip().split(",")
    kmtasu = float(sõne[2]) * s
    kokku = kmtasu + float(sõne[1])
    if kokku < kokkufirma:
        kokkufirma = kokku
        odavaim = sõne[0]
print("Kõige odavam on " + odavaim + ".")
file.close()