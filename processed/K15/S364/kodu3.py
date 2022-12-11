f = open(input('Sisesta failinimi: '))
bussid = []
sobivad_bussid = []
for rida in f:
    valjumisaeg, saabumisaeg, price = rida.split(';')
    price = price.strip()
    bussid +=  [[valjumisaeg, saabumisaeg, price]]
for bus in bussid:
    sobivad_bussid += [bus]
for bus in bussid:
    for bus_2 in bussid:
         if bus[0] < bus_2[0] and bus[1] > bus_2[1] and int(bus_2[2]) > int(bus_2[2]):
             sobivad_bussid.remove(bus)
             break

for i in range(0, len(sobivad_bussid)-1):
    for j in range(1, len(sobivad_bussid)):
        if sobivad_bussid[j][0] < sobivad_bussid[i][0]:
            sobivad_bussid[j], sobivad_bussid[i] = sobivad_busid[i], sobivad_busid[j]

print('Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse:')