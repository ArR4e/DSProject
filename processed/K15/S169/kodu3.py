def loeandmed(nimi):
    bussid = []
    fail = open(nimi,"r",encoding="utf-8")
    for a in fail.readlines():
        bussid.append(a.strip())
    return bussid

sisend = input("Sisesta fail: ")
sobivad = []
for a in loeandmed(sisend):
    andmeda = a.split(" ")
    for b in loeandmed(sisend):
        andmedb = b.split(" ")
        if andmeda[0] > andmedb[0] and andmeda[1] < andmedb[1] and int(andmeda[2]) < int(andmedb[2]):
            if a not in sobivad:
                sobivad.append(a)

print("Sobivad bussid:")
for a in sobivad:
    print(a)
        
        