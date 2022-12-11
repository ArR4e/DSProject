# 3. Bussid

# väljumisaeg - vaeg
# saabumisaeg - saeg
# sõidu hind - hind
# esimene element - el1 ning teine element - el2


fail = input("Sisesta failinimi: ")
with open(fail) as f:
    print("Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse:")
    failiandmed = f.readlines()
    failiandmed.sort()
    ignore_set = set()
    for el1 in failiandmed:
        el1 = el1.strip()
        vaeg1, saeg1, hind1 = el1.split()
        hind1 = float(hind1)
        for el2 in failiandmed:
            el2 = el2.strip()
            vaeg2, saeg2, hind2 = el2.split()
            hind2 = float(hind2)
            if vaeg1 < vaeg2 and saeg1 > saeg2 and hind1 > hind2:
                ignore_set.add(el1)
        if el1 not in ignore_set:
            print(el1)
            
            
