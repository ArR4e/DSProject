nimi = input("Sisest failinimi: ")

with open(nimi) as f:
    sobivad = []

    for rida in f:
        korrastatud = rida.split()
        väljumine1  =korrastatud[0]
        saabumine1 = korrastatud[1]
        hind1 = float(korrastatud[-1])
        buss = True
        with open(nimi) as f:
            for rida in f:
                
                korrastatud2 = rida.split()
                if korrastatud2 == korrastatud:
                    continue
                väljumine2  =korrastatud2[0]
                saabumine2 = korrastatud2[1]
                hind2 = float(korrastatud2[-1])
                
                if väljumine2 > väljumine1 and saabumine2 < saabumine1 and hind2 < hind1:
                    buss = False
                    break



                    
                
        if buss == True:
                    
            sobivad.append(korrastatud)
                            
                    
                    
#sorteerin ja väljastan
print("Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse:")                                
sobivad.sort()
for elem in sobivad:
    print(" ".join(elem))
                          
                                
                            
                
                