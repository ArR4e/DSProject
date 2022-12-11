def seosta_lapsed_ja_vanemad(fail1, fail2):
    f = open(fail1, encoding = "UTF-8")
    e = open(fail2, encoding = "UTF-8")
    ds1 = {}
    ds2 = {}
    ds3 = {}
    vanemlist = []
    lapslist = []
       
        
    for rida2 in f:
        rida2 = rida2.strip().split()
        vanemisik = rida2[0]
        lapsisik = rida2[1]
        vanemlist.append(vanemisik)
        lapslist.append(lapsisik)

        
    for rida1 in e:
        rida1 = rida1.strip().split()
        isikukood = rida1[0]
        nimi = rida1[1] + " " + rida1[2]
        ds1[isikukood] = nimi
        if isikukood in lapslist:
            lapsnimi = ds1.get(isikukood)

            
        if isikukood in vanemlist:
            vanemnimi = ds1.get(isikukood)
        
    
 
    
        