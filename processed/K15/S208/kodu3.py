f = open(input("Sisesta faili nimi: "), encoding="utf-8")
print("Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse:")
bussid = []
for rida in f:
    sisu = rida.strip().split(" ")
    bussid.append(sisu)
bussid.sort()
def sorteer(bussid):
    for i in range(len(bussid)-1):
        if bussid[i][1] > bussid[i+1][1] and float(bussid[i][2]) > float(bussid[i+1][2]):
            del bussid[i]
            sorteer(bussid)
            break
sorteer(bussid)
uus = bussid
uus.sort()
for i in range(len(uus)):
    print(uus[i][0],uus[i][1],uus[i][2])
f.close()