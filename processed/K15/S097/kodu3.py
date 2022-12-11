fail = input("Sisesta failinimi: ")
f = open(fail, encoding = "UTF-8")

sobivadbussid = []
bussiajad = []

for buss in f:
    bussiajad.append(buss)
    sobivadbussid.append(buss)

for i in range(len(bussiajad)):
    väljumine = list(bussiajad[i].split(" "))[0]
    saabumine = list(bussiajad[i].split(" "))[1]
    pilet = float(list(bussiajad[i].split(" "))[2])  
    for j in range(len(bussiajad)):
        väljumine2 = list(bussiajad[j].split(" "))[0]
        saabumine2 = list(bussiajad[j].split(" "))[1]
        pilet2 = float(list(bussiajad[j].split(" "))[2])
        if väljumine2 > väljumine and saabumine2 < saabumine and pilet2 < pilet:
            sobivadbussid.remove(bussiajad[i])
            break
        else:
            continue
            
f.close()

sobivadbussid.sort()
print("Võiksid kaaluda järgmisi busse: ")
for buss in sobivadbussid:
    print(buss.strip())
    


    