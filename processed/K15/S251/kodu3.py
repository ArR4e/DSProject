sisend = input("Sisesta failinimi: ")

f = open(sisend,"r",encoding="utf-8")

kõik = []
eemaldamisele = []


while True:
    rida = f.readline()
    
    if rida == "":
        break
    
    rida = rida.strip("\n")
    
    kõik.append(rida)

for i in kõik:
    
    algus1 = int(i[:2] + i[3:5])
    lõpp1 = int(i[6:8] + i[9:11])
    hind1 = int(i[12:])
    
    for j in kõik:
        
        algus2 = int(j[:2] + j[3:5])
        lõpp2 = int(j[6:8] + j[9:11])
        hind2 = int(j[12:])
    
        if algus1 < algus2 and lõpp1 > lõpp2 and hind1 > hind2:
            eemaldamisele.append(i)
            break

for i in eemaldamisele:
    kõik.remove(i)
    
print("Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse: ")

sõnastik = {}
for i in kõik:
    sõnastik[int(i[:2] + i[3:5])] = i

järjekord = sorted(sõnastik)

for i in järjekord:
    print(sõnastik[i])

