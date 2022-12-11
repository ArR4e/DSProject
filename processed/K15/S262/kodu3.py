f = open(input("Sisestage failinimi: "), encoding="UTF-8")
andmed = []
for rida in f:
    sisu = rida.split(" ")
    väljumine = sisu[0].split(":")
    väljumisaeg = int(väljumine[0])*60+int(väljumine[1])
    kohalejõudmine = sisu[1].split(":")
    kohalejaeg = int(kohalejõudmine[0])*60+int(kohalejõudmine[1])
    hind = sisu[2]
    andmed.append([väljumisaeg,kohalejaeg,hind])

topVäljumine = 0
topVäljNr = 0
topSaabumine = 0
topSaabNr = 0
topHind = 0
topHindNr = 0

for el in range(len(andmed)):
    if andmed[el][0] >= topVäljumine:
        topVäljumine = andmed[el][0]
        topVäljNr = el
    if andmed[el][1] >= topSaabumine:
        topSaabumine = andmed[el][1]
        topSaabNr = el
    if int(andmed[el][2]) >= int(topHind):
        topHind = andmed[el][2]
        topHindNr = el
delete = []
if topVäljNr == topSaabNr:
    if topVäljNr == topHindNr:
        delete.append(topVäljNr)
    else:
        delete.append(topVäljNr)
        delete.append(topHindNr)
elif topVäljNr == topHindNr:
    delete.append(topVäljNr)
    delete.append(topSaabNr)
    
else:
    delete.append(topVäljNr)
    delete.append(topSaabNr)

for el in range(len(delete)):
    andmed.pop(el)

print("Esimesest linnast teise sõitmiseks võiksd kaaluda järgmisi busse:")

for el in range(len(andmed)):
    vm = int(andmed[el][0] % 60)
    vt = int((andmed[el][0]-vm)/60)
    sm = int(andmed[el][1] % 60)
    st = int((andmed[el][1]-sm)/60)
    hind = andmed[el][2]
    if vm == 0:
        vm = "00"
    if sm == 0:
        sm = "00"
    print(str(vt)+":"+str(vm),str(st)+":"+str(sm), str(hind))