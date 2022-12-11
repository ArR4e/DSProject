sisend = input("Sisesta failinimi: ")
fail = open(sisend)

hulk = set()
sisu = fail.readlines()
sisu.sort()
for rida in sisu:
    a = rida.strip("\n").split()
    välj = a[0]
    lõpp = a[1]
    hind = float(a[2])
    for teinerida in sisu:
        b = teinerida.strip("\n").split()
        välj2 = b[0]
        lõpp2 = b[1]
        hind2 = float(b[2])
        if välj < välj2 and lõpp > lõpp2 and hind > hind2:
            hulk.add(rida)
            
for i in sisu:
    if i not in hulk:
        print(i.strip())
    
fail.close()