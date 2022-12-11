fail = input("Sisesta faili nimi: ")
fail = "sõiduplaan.txt"
f = open("sõiduplaan.txt", encoding = "UTF-8")
lõplik = []
tervik = []
for rida in f:
    järjend = rida.strip().split(" ")
    tervik.append(järjend)
print("Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse:")
for i in range(len(tervik)):
    algus1 = tervik[i][0].split(":")
    lõpp1 = tervik[i][1].split(":")
    algustunnid1 = int(algus1[0])
    algusminutid1 = int(algus1[1])
    lõpptunnid1 = int(lõpp1[0])
    lõppminutid1 = int(lõpp1[1])
    alguskoos1 = algustunnid1 + algusminutid1/60
    lõppkoos1 =lõpptunnid1 + lõppminutid1/60
    hind1 = float(tervik[i][2])
    for j in range(len(tervik)):
        algus2 = tervik[j][0].split(":")
        lõpp2 = tervik[j][1].split(":")
        algustunnid2 = int(algus2[0])
        algusminutid2 = int(algus2[1])
        lõpptunnid2 = int(lõpp2[0])
        lõppminutid2 = int(lõpp2[1])
        alguskoos2 = algustunnid2 + algusminutid2/60
        lõppkoos2 =lõpptunnid2 + lõppminutid2/60
        hind2 = float(tervik[j][2])
        if alguskoos1 < alguskoos2 and lõppkoos1 > lõppkoos2 and hind1 > hind2:
            break
        if j == (len(tervik)-1):
            lõplik.append(tervik[i])
            continue

for a in range(len(lõplik)-1):
    for b in range(a+1, len(lõplik)):
        if lõplik[a] > lõplik[b]:
            lõplik[a], lõplik[b] = lõplik[b], lõplik[a]

for element in lõplik:
    sõne = " ".join(element)
    print(sõne)
        
        
        
    

    