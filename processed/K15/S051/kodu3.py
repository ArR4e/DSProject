def minutiteks(kellaaeg):
    aeg = kellaaeg.split(':')
    return int(aeg[0])*60 + int(aeg[1])

f = open(input("Sisesta failinimi: "), encoding="utf-8")
bussid = []
for rida in f:
    bussid.append(rida.strip('\n').split(' '))
f.close()

õiged_bussid = bussid[:]
for i in bussid:
    for j in range(len(bussid)):
        if minutiteks(i[0]) > minutiteks(bussid[j][0]) and minutiteks(i[1]) < minutiteks(bussid[j][1]) and i[2] < bussid[j][2]:
            õiged_bussid.remove(bussid[j])    

print("Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse:")
for buss in õiged_bussid:
    print(f"{buss[0]} {buss[1]} {buss[2]}")