def seosta_lapsed_ja_vanemad(laste_fail, nimede_fail):
    fail1 = open(laste_fail, encoding = "UTF-8")
    isikukoodid = []
    for rida in fail1:
        rida = rida.strip()
        rida = rida.split(" ")
        isikukoodid.append(rida)
    fail1.close()
    
    fail2 = open(nimede_fail, encoding = "UTF-8")
    isikukoodid_ja_nimed = []
    for rida in fail2:
        rida = rida.strip()
        rida = rida.split(" ", 1)
        isikukoodid_ja_nimed.append(rida)
    fail2.close()
    
    sõnastik = {}
    while isikukoodid != []:
        vanemate_isikukoodid = []
        lapse_nimi = ""
        vanemad = []
        lapse_id = isikukoodid[0][1]
        
        kordus = 0
        while kordus < len(isikukoodid):
            if lapse_id == isikukoodid[kordus][1]:
                vanemate_isikukoodid.append(isikukoodid[kordus][0])
            kordus += 1
            
        for j in range(len(vanemate_isikukoodid)):
            a = 0
            b = 0
            if vanemate_isikukoodid[j] == isikukoodid[a][0] and lapse_id in isikukoodid[b][1]:
                del isikukoodid[a]
                
                for i in range(len(isikukoodid_ja_nimed)):
                    if vanemate_isikukoodid[j] in isikukoodid_ja_nimed[i]:
                        vanemad.append(isikukoodid_ja_nimed[i][1])
                        
                for i in range(len(isikukoodid_ja_nimed)):
                    if lapse_id in isikukoodid_ja_nimed[i]:
                        lapse_nimi = isikukoodid_ja_nimed[i][1]
                
            else:
                for i in range(len(isikukoodid)):
                    if vanemate_isikukoodid[1] in isikukoodid[i][0] and lapse_id in isikukoodid[i][1]:
                        a = i
                        
                if vanemate_isikukoodid[j] == isikukoodid[a][0] and lapse_id in isikukoodid[a][1]:
                    del isikukoodid[a]
                    
                    for i in range(len(isikukoodid_ja_nimed)):
                        if vanemate_isikukoodid[j] in isikukoodid_ja_nimed[i]:
                            vanemad.append(isikukoodid_ja_nimed[i][1])
        
        sõnastik[lapse_nimi] = set(vanemad)
    return sõnastik
print(seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt"))