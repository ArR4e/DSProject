failinimi = input("Sisesta failinimi: ")

with open(failinimi, "r+") as f:
    bussiajad = f.readlines()

bussid = []

for rida in bussiajad:
    rida = rida.strip("\n").split(" ")
    bussid.append(rida)

for i in range(len(bussid)):
    for buss1 in bussid:
        for buss2 in bussid:
            if buss1[0] < buss2[0]:
                if buss1[1] > buss2[1]:
                    if float(buss1[2]) > float(buss2[2]):
                        try:
                            bussid.remove(buss1)
                        except:
                            continue
bussid.sort()

print("Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse: ")
for buss in bussid:
    print("{} {} {}".format(buss[0], buss[1], buss[2]))