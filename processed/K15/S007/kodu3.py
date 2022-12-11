failinimi = input("Sisestage failinimi: ")

fail = open(failinimi)
järjend = []
uus_järjend=[]
for rida in fail:
    rida = rida.strip()
    rida = rida.split(" ")
    
    järjend.append(rida)
    uus_järjend.append(rida)
for i in range(len(järjend)):
    for j in range(len(järjend)):
       if (järjend[i][0] <= järjend[j][0] and järjend[i][1] >= järjend[j][1] and int(järjend[i][2]) > int(järjend[j][2])):
            uus_järjend.remove(järjend[i])
            break
            
for i in range(len(uus_järjend)-1):
    for j in range(len(uus_järjend)-1):
        if uus_järjend[j][0] > uus_järjend[j+1][0]:
            uus_järjend[j], uus_järjend[j+1] = uus_järjend[j+1], uus_järjend[j]
            
            
print("Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse:")
for el in uus_järjend:
    print(el[0],el[1],el[2])
      
            

        