fail = open(input("Sisesta failinimi:"), encoding = 'utf-8')
bussid = []
sobib = []
for rida in fail:
    valjumisaeg, saabumisaeg, hind = rida.split(" ")
    hind = hind.strip()
    bussid += [[valjumisaeg, saabumisaeg, hind]]
for buss in bussid:
    sobib += [buss]
for buss in bussid:
    for buss2 in bussid:
        if buss[0] < buss2[0] and buss[1] > buss2[1] and int(buss[2]) > int(buss2[2]):
            sobib.remove(buss)
            break

for i in range(0, len(sobib) - 1):
    for j in range(i, len(sobib)):
        if sobib[j][0] < sobib[i][0]:
            sobib[j], sobib[i] = sobib[i], sobib[j]

print("Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse:")
        
for buss in sobib:
    print(buss[0], buss[1], buss[2])
   