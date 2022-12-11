f = open("taksohinnad.txt", encoding="UTF-8")
km = float(input("Sisesta tee pikkus kilomeetrites: "))

tekst = f.readlines()
odavaim_takso = ""
odavaim = 0
for rida in tekst:
    rida = rida.split(",")
    hind = float(rida[1]) + km * float(rida[2])
    if odavaim == 0:
        odavaim = hind
        odavaim_takso = rida[0]
    elif hind < odavaim:
        odavaim = hind
        odavaim_takso = rida[0]
print("Kõige odavam on", odavaim_takso + ".")
        