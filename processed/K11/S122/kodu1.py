def seosta_lapsed_ja_vanemad(f1,f2):
    laste_fail=open(f1,encoding="UTF-8")
    nimede_fail=open(f2,encoding="UTF-8")

    #loeb nimed ja isikukoodid faili
    pered={}
    inimesed={}
    for inimene in nimede_fail:
        inimene=inimene.strip().split(" ")
        inimese_kood= inimene[0]
        inimese_eesnimi = inimene[1]
        inimese_perenimi= inimene[2]
        inimesed[inimese_kood]=inimese_eesnimi + " "+inimese_perenimi
     
    nimede_fail.close()
    nimede_fail=open(f2,encoding="UTF-8")

    for inimene in nimede_fail:
        inimene=inimene.strip().split(" ")
        inimese_kood= inimene[0]
        inimese_nimi = inimesed[inimese_kood]
        for isik in laste_fail:
            koodid_eraldi=isik.strip().split(" ")
            vanem_kood=koodid_eraldi[0]
            laps_kood = koodid_eraldi[1]
            if laps_kood==inimese_kood:
                lapse_nimi = inimesed[laps_kood]
                pered[lapse_nimi] = None
                continue
            else:
                vanema_nimi = inimesed[vanem_kood]
                vanema_lapse_nimi = inimesed[laps_kood]
                if vanema_lapse_nimi not in pered:
                    pered[vanema_lapse_nimi] = vanema_nimi + ", "
                else:
                    pered[vanema_lapse_nimi] += vanema_nimi + ", "

    laste_fail.close()
    nimede_fail.close()

    return(pered)
     
        
