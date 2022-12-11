faili_nimi = input('sisesta bussigraafikute failinimi: ')
fail = open(faili_nimi)
head_bussid = []
bussi_info = []
for rida in fail:
    rea_järj = rida.rstrip().split(" ")
    bussi_info.append(rea_järj)
   
for i in range(len(bussi_info)):
    parem = True
    for j in range(len(bussi_info)):
        paar1 = bussi_info[i]
        paar2 = bussi_info[j]
        
        if paar1[0] < paar2[0] and paar1[1] > paar2[1] and int(paar1[2]) > int(paar2[2]):
            parem = False
            break
        
    if parem == True:  
        head_bussid.append(paar1)
        
muutsin = True
while muutsin:
    muutsin = False
    for i in range(len(head_bussid)-1):
        el1 = head_bussid[i]
        el2 = head_bussid[i+1]
        if el1[0] > el2[0]:
            head_bussid[i] = el2
            head_bussid[i+1] = el1
            muutsin = True

print("Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse:")
for buss in head_bussid:
    print(buss[0] + " " + buss[1] + " " + buss[2])
