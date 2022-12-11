sisend = input("Sisesta failinimi: ")
fail = open(sisend, encoding="UTF- 8")
jär = []
kiirem = 24
mitmes = 1
odavam = 9
for i in fail:
    buss = i.strip().split(" ")
    for k in buss:
        aeg = k.split(":")
        if len(aeg) == 2 and mitmes % 2 == 0:
            aeg[0] = float(aeg[0])
            kiirus2 = aeg[0] + (float(aeg[1]))/60
        elif len(aeg) == 2:
            aeg[0] = float(aeg[0])
            kiirus1 = aeg[0] + (float(aeg[1]))/60
        mitmes +=1
    if kiirus2-kiirus1 < kiirem:
        jär = [i.strip()]
        kiirem = kiirus2-kiirus1
    elif kiirus2-kiirus1 == kiirem:
        jär +=[i.strip()]
    kiirus1 = 0
    kiirus2 = 0
    mitmes = 1
    jär.sort()
print("Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse:")
for el in jär:
    print(el)
fail.close()