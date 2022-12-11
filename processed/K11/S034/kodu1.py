def seosta_lapsed_ja_vanemad(lastefailinimi,nimedefailinimi):
     #teeme tühja sõnastiku
    sõnastik = {}
    lapse_nimi = ""
    vanema_nimi = ""
    lapsed_mitmes_rida_praegu = 1
    loendus_nimi = 1
    lapse_isikukood = ""
    vanema_isikukood = ""
    loendus_kood = 0
     
    f = open(lastefailinimi)
    fread = (''.join(f.readlines())).split()

    g = open(nimedefailinimi)
    gread = (''.join(g.readlines())).split()
    
    #loeme mitu sõne on:
    lapsed_ridu = len(fread)
    nimed_ridu = len(gread)
 
    #leiame vanema nime
    while lapsed_mitmes_rida_praegu <= lapsed_ridu:
        for lrida in fread:
        #kui on paarisarv siis on lapse isikukood, kui pole ss vanema isikukood
            if lapsed_mitmes_rida_praegu % 2 == 0:
                lapse_isikukood = lrida
            else:
                vanema_isikukood = lrida
            lapsed_mitmes_rida_praegu += 1
            
            if lapse_isikukood != "" and vanema_isikukood != "":
                while lapse_nimi == "" or vanema_nimi == "":
                    if gread[loendus_kood] == vanema_isikukood:
                        vanema_nimi = gread[loendus_nimi] + " " + gread[loendus_nimi + 1]
                    elif gread[loendus_kood] == lapse_isikukood:
                        lapse_nimi = gread[loendus_nimi] + " " + gread[loendus_nimi + 1]
                    loendus_kood +=3
                    #lapsed_mitmes_rida_praegu += 1
                    loendus_nimi +=3
                #kui lapse nimi juba on sõnastikus siis lisame ühe vanema juurde hulka
                if lapse_nimi in sõnastik:
                     nimi = sõnastik[lapse_nimi]
                     sõnastik[lapse_nimi] = set(list(nimi) + [vanema_nimi])                     
                else:
                    sõnastik[lapse_nimi] = {vanema_nimi}
                lapse_nimi = ""
                lapse_isikukood = ""
                vanema_nimi = ""
                vanema_isikukood = ""
                loendus_nimi = 1
                loendus_kood = 0
                    
    return(sõnastik)
        
    f.close()
    g.close()