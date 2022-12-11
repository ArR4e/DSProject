from datetime import datetime

def ajavahe(s1, s2):
    FMT = '%H:%M'
    tdelta = datetime.strptime(s2, FMT) - datetime.strptime(s1, FMT)
    return tdelta.seconds / 3600

failinimi = input("Sisesta failinimi: ")

with open(failinimi, "r", encoding="UTF-8") as f:
    kellaajad = f.read().strip().split("\n")
    sobivad = kellaajad.copy()
    
    for i in range(len(kellaajad)):
        buss1 = kellaajad[i]
        algus, lõpp, hind = buss1.split()
        ajavahe1 = ajavahe(algus, lõpp)
        
        for j in range(len(kellaajad)):
            buss2 = kellaajad[j]
            algus2, lõpp2, hind2 = buss2.split()
            ajavahe2 = ajavahe(algus2, lõpp2)
            
            if ajavahe2 > ajavahe1 and int(hind2) > int(hind):
                try:
                    sobivad.remove(buss2)
                except:
                    continue

sobivad.sort()
print("Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse:", *sobivad
, sep="\n")