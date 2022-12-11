sisend = input("Sisesta failinimi: ")
fail = open(sisend, encoding="UTF-8")

ajad = []

for rida in fail:
    rida = rida.strip().split(" ")
    #rida[0] = float()
    rida[0] = int(rida[0].replace(":", ""))
    rida[1] = int(rida[1].replace(":", ""))
    rida[2] = int(rida[2])
    ajad.append(rida)
    
    for i in range(len(ajad)-1):
        for j in range(len(ajad)-1):
            if ajad[i][0] > ajad[j][0]:
                if ajad[i][1] < ajad[j][1]:
                    if ajad[i][2] < ajad[j][2]:
                        ajad.pop(j)

print("Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse: ")
print(ajad)
            
        

    
    