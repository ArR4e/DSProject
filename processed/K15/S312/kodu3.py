def valibuss(fail):
    f=open(fail)
    sobiv = []
    bussid = []
    for rida in f:
        tükid = rida.strip().split(' ')
        väljub = tükid[0]
        saabub = tükid[1]
        hind = int(tükid[2])
        bussid.append((väljub,saabub,hind))
    for i in range(len(bussid)):
        buss1 = bussid[i]
        sobivb = True
        for j in range(len(bussid)):
            buss2 = bussid[j]
            if buss2[0] > buss1[0] and buss2[1] < buss1[1] and buss2[2] < buss1[2]:
                sobivb = False    
        if sobivb == True:    
            sobiv.append(buss1)
    f.close()        
    return sobiv        
    



fail = input('Sisesta failinimi: ')
bussid = valibuss(fail)

for i in range(len(bussid)):
        for j in range(i+1, len(bussid)):
            if bussid[j][0] < bussid[i][0]:
                bussid[i], bussid[j] = bussid[j], bussid[i]

print('Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse:')
for i in bussid:
    print(i[0] + ' ' + i[1] + ' ' + str(i[2]))
    
