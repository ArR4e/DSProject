def seosta_lapsed_ja_vanemad(fail_id,fail_nimed):
    f_id = open(fail_id,"r")
    f_nimed = open(fail_nimed,"r",encoding="utf-8")
    #isikukood vastab nimele
    d_nimi_id = dict()
    for rida in f_nimed:
        sisu = rida.strip("\n").split(" ")
        d_nimi_id[sisu[0]]= (sisu[1] +" "+ sisu[2])
    f_nimed.close()
    
    lõpp_d = dict()
    võti = d_nimi_id.keys()
    nimi = d_nimi_id.values()
    võti = list(võti)
    nimi = list(nimi)
    for rida in f_id:
        sisu = rida.strip("\n").split(" ")
        #pnimi = sisu[1].split(" ")
        #perenimi = d_nimi_id[pnimi[0]].split(" ")
       
    
        vanem1 = d_nimi_id[sisu[0]]
        laps = d_nimi_id[sisu[1]]
        
        
        if laps in lõpp_d.keys():
            vanem2= lõpp_d[laps]
            vanem2.add(vanem1)
            lõpp_d[laps] = vanem2
        else:
            vanemad = set()
            vanemad.add(vanem1)
            lõpp_d[laps] = vanemad
    f_id.close()        
    return lõpp_d
                
print(seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt"))

