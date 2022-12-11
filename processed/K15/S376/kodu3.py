from datetime import datetime

def ajavahe(s1, s2):
    FMT = '%H:%M'
    tdelta = datetime.strptime(s2, FMT) - datetime.strptime(s1, FMT)
    return tdelta.seconds / 3600

failinimi = input("Sisesta failinimi: ")

with open(failinimi, "r", encoding="UTF-8") as f:
    ajad = f.read().strip().split("\n")
    sobivad = ajad.copy()
    
    for i in range(len(ajad)):
        buss1 = ajad[i]
        algus1, lõpp1, hind1 = buss1.split()
        ajavahe1 = ajavahe(algus1, lõpp1)
        
        for j in range(len(ajad)):
            buss2 = ajad[j]
            algus2, lõpp2, hind2 = buss2.split()
            ajavahe2 = ajavahe(algus2, lõpp2)
            
            if ajavahe2 > ajavahe1 and int(hind2) > int(hind1):
                try:
                    sobivad.remove(buss2)
                except:
                    continue

sobivad.sort()
print("Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse:", *sobivad, sep="\n")