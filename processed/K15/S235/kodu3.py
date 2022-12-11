fail = input("Sisestage failinimi: ")

f = open(fail, "r", encoding = "UTF-8")

bussid = []
for read in f:
    rida = read.strip().split(" ")
    väljumine = rida[0]
    saabumine = rida[1]
    hind = int(rida[2])
    buss = []
    buss.append(väljumine)
    buss.append(saabumine)
    buss.append(hind)
    bussid.append(buss)

print("Esimesest linnast teise sõitmiseks võiksite kaaluda järgimisi busse:")

head_bussid = []
for i in range(len(bussid)):
    sobib = True
    for j in range(len(bussid)):
        if bussid[i][0] < bussid[j][0] and bussid[i][1] > bussid[j][1]:
            if bussid[i][2] > bussid[j][2]:
                sobib = False
        else:              
            continue
        
    if sobib == True:
        head_bussid.append(bussid[i])

head_bussid.sort()
for i in range(len(head_bussid)):
    print(head_bussid[i][0], head_bussid[i][1], head_bussid[i][2])
