fail=input('Sisesta failinimi: ')
with open(fail) as f:
    sobivad=[]
    bussid=[]
    for rida in f:
        (väljumine, saabumine, hind) =rida.strip().split(' ')
        hind=int(hind)
        bussid.append([väljumine, saabumine, hind])
    bussid.sort()
    for buss in bussid:
        for buss2 in bussid:
            if buss!=buss2:
                if buss[0]>buss2[0]:
                    if buss[1]<buss2[1]:
                        if buss[2]<buss2[2]:
                            bussid.remove(buss2)
    for buss in bussid:
        for buss2 in bussid:
            if buss!=buss2:
                if buss[0]>buss2[0]:
                    if buss[1]<buss2[1]:
                        if buss[2]<buss2[2]:
                            bussid.remove(buss2)
                            
print('Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse: ')
for el in bussid:
    print(*el)
    
                    
            
                        
        
        