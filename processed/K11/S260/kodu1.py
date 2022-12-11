def seosta_lapsed_ja_vanemad(laste_fail,nime_fail):
    lapsed_f = open(laste_fail,"r")
    nimed_f = open(nime_fail,"r")
    
    lapsed_data = lapsed_f.readlines()
    nimed_data = nimed_f.readlines()
    
    lapsed_f.close()
    nimed_f.close()
    
    lapsed_1 = []
    lapsed_2 = []
    
    nimed_1 = []
    nimed_2 = []
    
    global lapse_nimed_1
    lapse_nimed_1 = []
    global lapse_nimed_2
    lapse_nimed_2 = []
    
    for rida in lapsed_data:
        lapsed_1.append(rida.strip().split()[0])
        lapsed_2.append(rida.strip().split()[1])
        
    for rida in nimed_data:
        nimed_1.append(rida.strip().split()[0])
        nimed_2.append(rida.strip()[12:])  
    
    for i in range(len(lapsed_1)):
        lapse_nimed_1.append(nimed_2[nimed_1.index(lapsed_1[i])])
    for i in range(len(lapsed_2)):
        lapse_nimed_2.append(nimed_2[nimed_1.index(lapsed_2[i])])        
    
    lapsed = {}
    lapsed_vanemad = {}
    
    for i in range(len(lapse_nimed_1)):
        lapsed[lapse_nimed_2[i]] = lapse_nimed_1[i]
    
    for nimi in set(lapsed):
        vanemad = []
        for i in range(len(lapse_nimed_1)):
            if nimi == lapse_nimed_1[i] and nimi not in lapsed:
                vanemad.append(lapse_nimed_2[i])
            if nimi == lapse_nimed_2[i]:
                vanemad.append(lapse_nimed_1[i])
        lapsed_vanemad[nimi] = set(vanemad)
        #print(nimi+":",", ".join(vanemad))

    return lapsed_vanemad
    
seosta_lapsed_ja_vanemad("lapsed.txt","nimed.txt")
