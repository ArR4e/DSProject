teepikkus = int(input("Sisesta tee pikkus kilomeetrites: "))
fail = open("taksohinnad.txt")
for rida in fail:
    read = rida.split(",")
    stardihind = read[1]
    kilomeetri_hind = read[2]
    hind = str(float(stardihind) + float(kilomeetri_hind)*teepikkus)
    takso = []
    takso.append(hind)
    print(takso)
    takso_nimi = []
    takso_nimi.append(read[0])
fail.close()