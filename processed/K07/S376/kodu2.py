km = float(input("Sisesta tee pikkus kilomeetrites: "))
odavaim_tasu = 0.0
odavaim_takso = ""

f = open("taksohinnad.txt", "r", encoding="UTF-8")

for rida in f:
    rida = rida.strip()
    eraldi = rida.split(",")
    
    nimi = eraldi[0]
    alustustasu = float(eraldi[1])
    km_tasu = float(eraldi[2])
    
    tasu_kokku = alustustasu + km_tasu * km
    
    if odavaim_tasu == 0:
        odavaim_tasu = tasu_kokku
    if tasu_kokku <= odavaim_tasu:
        odavaim_tasu = tasu_kokku
        odavaim_takso = nimi

print("Kõige odavam on", odavaim_takso)

f.close()