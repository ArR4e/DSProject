f = input("Sisesta failinimi: ")
fail = open(f, encoding="UTF-8")

print("Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse: ")

bussid = []
for r in fail:
    bussid.append(r.split())
fail.close()
#fail = open("sõiduplaan.txt", encoding="UTF-8")


sobivad =  []
for i in range(len(bussid)):
    sobib = True
    for j in range(len(bussid)):
        if bussid[i][1] > bussid[j][1]:
            if bussid[i][0] < bussid[j][0]:
                if int(bussid[i][2]) > int(bussid[j][2]):
                    sobib = False
    if sobib == True:
        sobivad.append(bussid[i])

for ee in sobivad:
    print(" ".join(map(str, ee)))