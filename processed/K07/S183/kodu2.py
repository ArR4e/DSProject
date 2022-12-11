fail = open("taksohinnad.txt", encoding="UTF- 8")
tee_pikkus = float(input("Sisesta tee pikkus kilomeetrites: "))
takso_hind = []
nimi = []

for rida in fail:
    takso = rida.split(",")
    hind = float(takso[1]) + tee_pikkus * float(takso[2])
    takso_hind.append(hind)
    nimi.append(takso[0])


if takso_hind == []:
    print("0")
else:
    väiksem = min(takso_hind)
    indeks = takso_hind.index(väiksem)
    print(f"Kõige odavam on {nimi[indeks]}")

fail.close()