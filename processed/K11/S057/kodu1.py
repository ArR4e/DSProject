def seosta_lapsed_ja_vanemad(failinimi_lapsed, failinimi_nimed):
    vlandmed_fail = open(failinimi_lapsed)
    nimed_fail = open(failinimi_nimed)
    nimed_sõnastik = {}
    for rida in nimed_fail:
        rida = rida.strip().split(" ")
        isikukood = rida[0]
        nimi = rida[1] + " " + rida[2]
        nimed_sõnastik[isikukood] = nimi
    lvsõnastik = {}
    loetud_laste_nimed = []
    for rida in vlandmed_fail:
        rida = rida.strip().split(" ")
        ik_vanem = rida[0]
        ik_laps = rida[1]
        vanema_nimi = nimed_sõnastik[ik_vanem]
        lapse_nimi = nimed_sõnastik[ik_laps]
       # if lapse_nimi in loetud_laste_nimed:
        #    lvsõnastik[lapse_nimi] = lvsõnastik[lapse_nimi].append(vanema_nimi)
        loetud_laste_nimed += [lapse_nimi]
        lvsõnastik[lapse_nimi] = set([vanema_nimi]) #viimasena; vanemate nimed on HULK ehk SET
    print(lvsõnastik)
    return lvsõnastik
    
seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt")