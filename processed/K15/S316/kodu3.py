fail = open(input("Sisesta failinimi: "))

sobivad_bussid = []
for rida in fail:
    sobib = 0
    buss1 = rida.strip().split(" ")
    for rida2 in fail:
        buss2 = rida2.strip().split(" ")
        if buss1[2] < buss2[2]:
            sobib = True
        else:
            sobib = False
        if buss1[0] > buss2[0]:
            sobib = True
        else:
            sobib = False
        if buss1[1] < buss2[1]:
            sobib = True
        else:
            sobib = False
        if sobib == True:
            if buss1 in sobivad_bussid:
                continue
            else:
                sobivad_bussid.append(buss1)
        if sobib == False:
            if buss2 in sobivad_bussid:
                continue
            else:
                sobivad_bussid.append(buss2)

fail.close()

sobivad_bussid.sort()
print("Sobivad väljuvad bussid: ")
for element in sobivad_bussid:
    print(element[0], element[1], element[2])