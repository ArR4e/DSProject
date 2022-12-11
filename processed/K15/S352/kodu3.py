fail=input("Sisesta failinimi: ")
bussid=[]

with open(fail, encoding="utf8") as f:
    for rida in f:
        bussid.append(rida.split())
sobivad_bussid=bussid[:]

for i in range(len(bussid)):
    for j in range(len(bussid)):
        if bussid[i][0]<bussid[j][0] and bussid[i][1]>bussid[j][1] and int(bussid[i][2])>=int(bussid[j][2]):
            if bussid[i] in sobivad_bussid:
                sobivad_bussid.remove(bussid[i])

print("Mõtet on kaaluda järgnevaid busse:")
for buss in sorted(sobivad_bussid):
    for el in buss:
        print(el,end=" ")
    print()