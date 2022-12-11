sisend = input("Sisesta failinimi: ")
fail = open(sisend, encoding = "utf-8")

hulk_ignore = set()
sisu = fail.readlines()
sisu.sort()
for rida in sisu:
    a = rida.strip("\n").split(" ")
    valj = a[0]
    lopp = a[1]
    hind = float(a[2])
    for teinerida in sisu:
        b = teinerida.strip("\n").split(" ")
        valj2 = b[0]
        lopp2 = b[1]
        hind2 = float(b[2])
        if valj < valj2 and lopp > lopp2 and hind > hind2:
            hulk_ignore.add(rida)
            
for i in sisu:
    if i not in hulk_ignore:
        print(i.strip())
    
fail.close()