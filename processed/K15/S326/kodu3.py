fail = input("Sisesta failinimi: ")

fail = open(fail)
sisu = fail.readlines()
andmed = []
for sõit in sisu:
    sõit = sõit.strip().split(" ")
    andmed.append(sõit)
print("Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse: ")
for i in range(3):
    parim = andmed[0]
    for sõit in andmed:
        if sõit[0] > parim[0] and sõit[1] < parim[1] and sõit[2] < parim[2]:
            parim = sõit
    print(" ".join(parim))
    andmed.remove(parim)