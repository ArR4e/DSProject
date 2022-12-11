#Valib tekstifailist välja parimad bussiajad

f = open(input("Palun sisestage failinimi: "))
sisu = f.readlines()
f.close()

print("Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse:")

graafik = []
for rida in sisu:
    rida = rida.strip().split(" ")
    graafik.append(rida)

sobivad = []
for buss1 in graafik:
    sobib = True
    for buss2 in graafik:
        if buss1[0] < buss2[0] and buss1[1] > buss2[1] and int(buss1[2]) > int(buss2[2]):
            sobib = False
    if sobib:
        sobivad.append(buss1)
    else:
        continue

sobivad = sorted(sobivad, key=lambda x: x[0], reverse=False)
for buss in sobivad:
    print(buss[0], buss[1], buss[2])
        