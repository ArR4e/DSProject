f = open(input("Sisesta failinimi "), encoding = "utf-8")
bussid = []
sobivad_bussid = []
for rida in f:
    valjumisaeg, saabumisaeg, hind = rida.split(" ")
    hind = hind.strip()
    bussid += [[valjumisaeg, saabumisaeg, hind]]
for buss in bussid:
    sobivad_bussid += [buss]
for buss in bussid:
    for buss2 in bussid:
        if buss[0] < buss2[0] and buss[1] > buss2[1] and int(buss[2]) > int(buss2[2]):
            sobivad_bussid.remove(buss)
            break

for i in range(0, len(sobivad_bussid)-1):
    for j in range(i, len(sobivad_bussid)):
        if sobivad_bussid[j][0]<  sobivad_bussid[i][0]:
            sobivad_bussid[j], sobivad_bussid[i] = sobivad_bussid[i], sobivad_bussid[j]

print("Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse:")

for buss in sobivad_bussid:
    print(buss[0], buss[1], buss[2])