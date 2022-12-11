def seosta_lapsed_ja_vanemad(lapse_fail, nime_fail):
    
    lapsed_fail = open(lapse_fail, "r")
    koodid_jrj=[]
    for rida in lapsed_fail:
        
        koodid = tuple(rida.split(" "))
        koodid_jrj.append(koodid)
    
    lapsed_fail.close()
    
    nimed_fail = open(nime_fail, "r")
    nimed_dict={}
    for rida in nimed_fail:
        
        nimed_koodid = rida.split(" ")
        nimi = nimed_koodid[1]+" "+nimed_koodid[2].strip()
        nimed_dict[nimed_koodid[0].strip()]=nimi
    
    nimed_fail.close()
    
    lõpp_dict={}
    
    for i in range(len(koodid_jrj)):
        laps_nimi = nimed_dict[koodid_jrj[i][1].strip()]
        vanem_nimi = nimed_dict[koodid_jrj[i][0].strip()]
        
        if laps_nimi in lõpp_dict:
            lõpp_dict[laps_nimi].add(vanem_nimi)
        else:
            lõpp_dict[laps_nimi]=set()
            lõpp_dict[laps_nimi].add(vanem_nimi)

    return lõpp_dict
    
sõnastik = seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt")

for key in sõnastik:
    print(key,": " ,sep="", end="")
    
    if len(sõnastik[key])==2:
        listina = list(sõnastik[key].copy())
        print(listina[0], ", ", sep="", end="")
        print(listina[1])
    elif len(sõnastik[key])==1:
        listina = list(sõnastik[key].copy())
        print(listina[0])