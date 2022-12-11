fail=open(input("Sisesta failinimi: "))
sobivad_bussid=[]

for rida in fail:
    sobib=0
    esimene_buss=rida.strip().split(" ")
    for rida2 in fail:
        teine_buss=rida2.strip().split(" ")
        if esimene_buss[2]<teine_buss[2]:
            sobib=True
        else:
            sobib=False
        if esimene_buss[0]>teine_buss[0]:
            sobib=True
        else:
            sobib=False
        if sobib==True:
            if esimene_buss in sobivad_bussid:
                continue
            else:
                sobivad_bussid.append(esimene_buss)
        if sobib==False:
            if teine_buss in sobivad_bussid:
                continue
            else:
                sobivad_bussid.append(teine_buss)
fail.close()

sobivad_bussid.sort()
print("Sobivad väljuvad bussid: ")
for element in sobivad_bussid:
    print(element[0], element[1], element[2])
    