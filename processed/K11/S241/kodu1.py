def seosta_lapsed_ja_vanemad(fail1, fail2):    
    sõnastik_nimed = {} # tühi sõnastik
    with open(fail1) as fail_nimed: #avab faili nimed.txt 
        for rida in fail_nimed: # loeb ridahaaval sellest failist
            (ik, nimi) = rida.strip().split(' ',1) #iga rea poolitab tühiku kohalt ja omistab esimese väärtuse ik-le, teise eesnimi-le, kolmanda perenimi-le
            sõnastik_nimed[ik] = nimi # sõnastik_nimed saab võtme väärtuse kohal ik väärtuse eesnimi + tühik + perenimi
#    print("Sõnastik nimed ", sõnastik_nimed, '\n')

    sõnastik_ik = {}
    with open(fail2) as fail_ik: #avab faili lapsed.txt 
        for rida in fail_ik: # loeb ridahaaval sellest failist
            (ik_vanem, ik_laps) = rida.split() #iga rea poolitab tühiku kohalt ja omistab esimese väärtuse ik-le, teise eesnimi-le, kolmanda perenimi-le
            sõnastik_ik[ik_vanem] = ik_laps # sõnastik_nimed saab võtme väärtuse kohal ik väärtuse eesnimi + tühik + perenimi
#    print("Sõnastik_ik ", sõnastik_ik, '\n')

    uus_sõnastik = {} 
    for vanema_ik, lapse_ik in sõnastik_ik.items(): 
        lapse_ik = sõnastik_ik[vanema_ik] # muutujasse lapse_ik lähevad laste isikukoodid
        lapse_nimi = sõnastik_nimed[lapse_ik] # muutujasse lapse_nimi lähevad laste nimed
#        print(lapse_nimi)
        # järgmise sammuna on vaja lapse isikukoodile seada vastavusse tema vanema isikukood
        # vanema isikukood on võti sõnastikus sõnastik_ik, lapse isikukood on samas sõnastikus väärtuse kohal
        for van_ik, laps_ik in sõnastik_ik.items(): # sõnastik_ik liikmete läbivaatamine, van_ik on vanema ik ja laps_ik on lapse ik
            if laps_ik == lapse_ik: # lapse_ik oli teadaolevalt lapse isikukood ja kui laps_ik on sellega identne, siis on see lapse IK
                lapsevanema_ik = van_ik # järelikult on van_ik just selle lapse vanema isikukood ja omistatakse uuele muutujale
                uus_sõnastik[laps_ik] = lapsevanema_ik # mõte jäi kinni ikkagi pööratud sõnastiku juurde, nagu ülevalpool näha, ja see ei tööta nagu vaja
    return uus_sõnastik 

print(seosta_lapsed_ja_vanemad('nimed.txt', 'lapsed.txt'))