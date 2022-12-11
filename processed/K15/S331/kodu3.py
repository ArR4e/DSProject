failinimi = input("Sisesta failinimi:")
f = open(failinimi, encoding = "utf-8-sig")
buss = []
bussid = []
while True:
    rida = f.readline().strip()
    if rida =="":
        break
    järjend = rida.split(" ")
    algus = järjend[0]
    lõpp = järjend[1]
    hind = järjend[2]
    buss.append(algus)
    buss.append(lõpp)
    buss.append(hind)
    bussid.append(buss)
    buss = []
f.close()
bussid.sort()
for buss1 in bussid:
    for buss2 in bussid:
        if buss1[0] < buss2[0] and buss1[1] > buss2[1] and buss1[2] > buss2[2]:
            print(" ".join(buss2))
        
    