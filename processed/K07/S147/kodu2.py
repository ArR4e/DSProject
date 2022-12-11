km = float(input("Sisestage tee pikkus kilomeetrites: "))
taksohinnad = open("taksohinnad.txt")
odavaim = 100000
for rida in taksohinnad:
    rida = rida.split(",")
    takso_nimi = rida[0]
    sisse_istumine = float(rida[1])
    km_hind = float(rida[2])
    summa = sisse_istumine+km*km_hind
    if summa < odavaim:
        odavaim = summa
        odavaim_takso = takso_nimi
taksohinnad.close()
print(f"Kõige odavam on {odavaim_takso}.")