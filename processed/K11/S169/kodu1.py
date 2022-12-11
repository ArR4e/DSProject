def seosta_lapsed_ja_vanemad(fail1,fail2):
    f1 = open(fail1,"r",encoding = "utf-8")
    f2 = open(fail2,"r",encoding = "utf-8")
    vanem_laps=[]
    isikud = {}
    lapsed_vanematega = {}

    for a in f1.readlines():
        vanem_laps.append(a.strip())
        
    for b in f2.readlines():
        a = " "
        isik = b.strip().split(" ")
        isikud[isik[0]]=a.join(isik[1:])

    for x in vanem_laps:
        hulk = set()
        if isikud[x.split()[1]] not in lapsed_vanematega:
            lapsed_vanematega[isikud[x.split()[1]]] = hulk
    for y in vanem_laps:
        lapsed_vanematega[isikud[y.split()[1]]].add(isikud[y.split()[0]])
    return lapsed_vanematega

sõnastik = seosta_lapsed_ja_vanemad("lapsed.txt","nimed.txt")
for a in sõnastik:
    b = ", "
    print(a+": "+b.join(sõnastik[a]))
        
        