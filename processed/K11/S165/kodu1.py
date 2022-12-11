def failist_sõnastikuks(faili_nimi):
    f_nimed = open(faili_nimi, "r", encoding = "UTF-8")
    nimed = f_nimed.readlines()
    nime_dict = {}
    
    for el in nimed:
        isikukood = el.split(" ", 1)[0]
        nimi = el.split(" ", 1)[1].strip()
        nime_dict[isikukood] = nimi
    
    return nime_dict



def seosta_lapsed_ja_vanemad(lapsed_fail,nimed_fail):
    f_lapsed = open(lapsed_fail, "r", encoding = "UTF-8")
    lapsed = f_lapsed.readlines()
    
    nime_dict = failist_sõnastikuks(nimed_fail)
    
    d = {}
    
    for i in range(len(lapsed)):
        lapse_isikukood = lapsed[i].strip().split(" ")[1]
        vanema_isikukood = lapsed[i].strip().split(" ")[0]
        hulk = set()
        
        vanemad = d.get(nime_dict[lapse_isikukood], set())
        vanemad.add(nime_dict[vanema_isikukood])
        
        d[nime_dict[lapse_isikukood]] = vanemad
        
    
    return d
    
sõnastik = seosta_lapsed_ja_vanemad("lapsed.txt","nimed.txt")   

for laps in sõnastik:
   vanemad = ""
   for vanem in sõnastik[laps]:
           vanemad = vanemad  + ", " + vanem 
       
   print(laps +":", vanemad)




   
   
   