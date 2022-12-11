tee = float(input("Sisestage tee pikkus kilomeetrites: "))
fail = open("taksohinnad.txt")
odavaim = 9**99
odav_nimi = ""
for line in fail.readlines():
    line = line.split(",")
    if float(line[1]) + float(line[2]) * tee < odavaim:
        odav_nimi = line[0]
        odavaim = odavaim * 0 + float(line[1]) + float(line[2]) * tee
    else:
        continue
print(f"Kõige odavam on {odav_nimi}.")