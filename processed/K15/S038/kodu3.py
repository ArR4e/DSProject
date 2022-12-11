nimetus = input("Sisestage failinimi: ")

fail = open(nimetus)
values = []

for line in fail:
    line2 = line.strip("\n")
    line3 = line2.lstrip()
    values.append(line3.split(" "))
    

def arvutus(aeg):
    v2ljumine = str(aeg[0]).split(":")
    saabumine = str(aeg[1]).split(":")
    minutid = (int(v2ljumine[0])*60)+ int(v2ljumine[1])
    minutid2 = (int(saabumine[0])*60) + int(saabumine[1])
    vahe = minutid2 - minutid
    return vahe

i = 1
while i < len(values):
    if arvutus(values[i]) > arvutus(values[i-1]):
        del values[i]
    else:
        i += 1

print("Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse: ")

for el in values:
    buss = " "
    bussid = buss.join(el)
    print(bussid)
    
    
    

