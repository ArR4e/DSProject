def seosta_lapsed_ja_vanemad(laste_fail, nimede_fail):
    f1 = open(laste_fail, "r", encoding="utf-8")
    f2 = open(nimede_fail, "r", encoding="utf-8")
    a = {}
    isikukoodi_järjend = []
    nimede_sõnastik = {}
    
    for rida in f1:
        idkood = rida.strip().split(' ')
        isikukoodi_järjend.append(idkood)
        
    for rida in f2:
        nimed = rida.strip().split(' ', 1)
        nimede_sõnastik[nimed[0]] = nimed[1]
        
    for el in isikukoodi_järjend:
        if nimede_sõnastik[el[1]] in a:
            a[nimede_sõnastik[el[1]]].add(nimede_sõnastik[el[0]])
        else:
            a[nimede_sõnastik[el[1]]] = set()
            a[nimede_sõnastik[el[1]]].add(nimede_sõnastik[el[0]])
    
    f1.close()
    f2.close()
    return a

sõnastik = seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt")
for i in sõnastik:
    vanematenimed = list(sõnastik[i])
    if len(sõnastik[i]) == 2:
        print(i + ": " + vanematenimed[0] + ", " + vanematenimed[1])
    else:
        print(i + ": " + vanematenimed[0])
        

