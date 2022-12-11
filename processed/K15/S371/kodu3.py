failinimi = input("Sisesta failinimi: ")

fail = open(failinimi, encoding = "UTF-8")

bussiajad = []
for rida in fail:
    rida = rida.strip()
    rida = rida.split()
    hind = rida[2]
    bussiajad.append(rida)
fail.close()
        
mittesobilikud = []
for i in range(len(bussiajad)):
    for j in range(len(bussiajad)):
        if bussiajad[i][0] > bussiajad[j][0] and bussiajad[i][1] < bussiajad[j][1] and float(bussiajad[i][2]) < float(bussiajad[j][2]):
            mittesobilikud.append(bussiajad[j])

for i in range(len(bussiajad)):
    for j in range(i, len(bussiajad)):
        if bussiajad[i][0] > bussiajad[j][0]:
            bussiajad[j], bussiajad[i] = bussiajad[i], bussiajad[j]

print("Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse:")
for i in bussiajad:
    if i not in mittesobilikud:
        väljumisaeg = i[0]
        saabumisaeg = i[1]
        hind = i[2]
        print(väljumisaeg, saabumisaeg, hind)
    
