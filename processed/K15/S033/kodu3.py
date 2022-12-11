failinimi = input("Sisesta failinimi: ")
f = open(failinimi, encoding = "utf-8")

bussid = []
for rida in f:
    rida = rida.strip().split(" ")
    start = rida[0]
    stop = rida[1]
    hind = int(rida[2])
    bussid.append((start, stop, hind))
    
sobivad = []
for buss in bussid:
    for buss2 in range(1, len(bussid)):
        if buss[0] > bussid[buss2][0] and buss[1] < bussid[buss2][1] and buss[2] <= bussid[buss2][2]:
            if buss not in sobivad:
                sobivad.append(buss)      
        
print("Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse:")
for i in sobivad:
    print(i[0] + " " + i[1] + " " + str(i[2]))
    
f.close()






    
