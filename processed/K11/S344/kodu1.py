def seosta_lapsed_ja_vanemad(lapsed, nimed):
    lapsed = open("lapsed.txt", "r")
    nimed = open("nimed.txt", "r")
    tulemus = {}
    kood = {}
    sõnastik = {}
    laps = set()
    vanemad = set()
    
    
    for rida in nimed:
        nimi = rida.strip()
        nimi = rida.split(" ", 1)
        sõnastik[nimi[0].strip()] = nimi[1].strip()
        lapse_nimi = sõnastik[nimi[0].strip()]
    #print(sõnastik)
        
    for rida in lapsed:
        isikukood = rida.split(" ")
        vanema_kood = isikukood[0].strip()
        lapse_kood = isikukood[1].strip()
        #print(vanema_kood)
        lapse_nimi = sõnastik[lapse_kood]
        vanema_nimi = sõnastik[vanema_kood]
        #print(lapse_nimi)
        
        vanemad = set()
        if lapse_nimi not in tulemus:
            vanemad.add(vanema_nimi)
            tulemus[lapse_nimi] = vanemad
            #tulemus.add(lisa) 
            #print(lisa)
        else:
            vanemad = tulemus[lapse_nimi]
            vanemad.add(vanema_nimi)
            tulemus[lapse_nimi] = vanemad
            #print(tulemus)
            #tulemus[lapse_nimi] = lisa
        #kood[vanema_kood] = lapse_kood
    #print(kood)
        
#         for rida in nimed:
#             nimi = rida.strip()
#             nimi = rida.split(" ", 1)
#             sõnastik[nimi[0]] = nimi[1]
#             lapse_nimi = sõnastik[nimi[0]]
#             print(sõnastik)
        
#     for a, b in kood.items():
#             vanemad = tulemus.get(vanema_kood, set())
#             vanemad.add(lapse_nimi)
#             tulemus[vanema_kood] = vanemad
#             return tulemus
#            if kood[vanema_kood] in sõnastik[nimi[0]]:
#                 vanemad.add((kood, sõnastik))
#             if kood[lapse_kood] in sõnastik[nimi[0]]:
#                 laps.add((kood, sõnastik))
            
         
    #tulemus[lapse_nimi] = vanemad
    #print(kood)    
    #print(sõnastik)
    return tulemus
            

print(seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt"))