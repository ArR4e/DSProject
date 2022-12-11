failinimi=input("Sisesta failinimi: ")


sõidud = open(failinimi, "r")
andmed=[]
for rida in sõidud:
    
    rida1=rida.strip()
    ajad_jrj=rida1.split(" ")
    
    andmed.append((ajad_jrj))
    
lõpp=[]
for i in range(len(andmed)):
    sobib=True
    
    for j in range(len(andmed)):

        if andmed[i][0]<andmed[j][0] and andmed[i][1]>andmed[j][1]:
            if int(andmed[i][2])>int(andmed[j][2]):  
                sobib=False
                
    
    if sobib==True:
        lõpp.append(andmed[i])
                    
            
lõpp.sort()            
print("Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse:\n")       
for buss in lõpp:
    for ajad in buss:
        print(ajad, end=" ")
    print("\n")
