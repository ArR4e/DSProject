def seosta_lapsed_ja_vanemad(f1, f2):
    f_lapsed = open(f1, encoding="UTF-8")
    f_nimed = open(f2, encoding="UTF-8")
    sõnastik = {}
    sõnastik1 = {}
    sõnastik2 = {}
    uus_rida1 = []
    uus_rida2 = []
    laste_koodid = []
    
    for rida1 in f_lapsed:
        rida1 = rida1.split(" ",2)
        rida1[-1] = rida1[-1].strip()
        uus_rida1.append(rida1)
        laste_koodid.append(rida1[1])
        
        for i in range(len(uus_rida1)):
            sõnastik1[uus_rida1[i][0]] = uus_rida1[i][1]
        
        
    for rida2 in f_nimed:
        rida2 = rida2.strip("\n").split(" ",1)
        uus_rida2.append(rida2)
    for i in range(len(uus_rida2)):
        sõnastik2[uus_rida2[i][0]] = uus_rida2[i][1]
    
    
    for k in range(len(laste_koodid)):
        vanema_kood = list(sõnastik1.keys())[list(sõnastik1.values()).index(laste_koodid[k])]
        vanema_nimi = sõnastik2[vanema_kood]
        lapse_nimi = sõnastik2[laste_koodid[k]]

        if lapse_nimi not in sõnastik:
            sõnastik[lapse_nimi] = set()
            sõnastik[lapse_nimi].add(vanema_nimi)
        else:
            sõnastik[lapse_nimi].add(vanema_nimi)
            
        
            
        
        
    
    f_lapsed.close()
    f_nimed.close()

    print(sõnastik)
    
   
    
print(seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt"))