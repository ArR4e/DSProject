teepikkus_koju = int(input("Sisesta teepikkus koju kilomeetrites: "))

f = open("taksohinnad.txt")
odavam_takso = ("", 0)
for rida in f:
    #print(rida)
    osad = rida.split(",")
    nimi = osad[0]
    alustus_tasu = float(osad[1])
    km_hind  = float(osad[2])
    hind = alustus_tasu + km_hind * teepikkus_koju
    if odavam_takso[1] == 0:
        odavam_takso = (nimi, hind)
    else:
        if hind < odavam_takso[1]:
            odavam_takso = (nimi, hind)

print("Kõige odavam on " + str(odavam_takso[0]) + ".")



f.close()

