def seosta_lapsed_ja_vanemad(lastefail, nimedefail):
    
    
    f = open("lapsed.txt", "r")
    sõnastik = {}
    for rida in f:
        isikukoodid = rida.split()
        for rida2 in isikukoodid:
            vanema_isikukood = isikukoodid[0]
            lapse_isikukood = isikukoodid[1]
            f2 = open("nimed.txt", "r")
            for rida3 in f2:
                ik = rida3.split()
                if vanema_isikukood == ik[0]:
                    vanemanimi = ik[1], ik[2]
                if lapse_isikukood == ik[0]:
                    lapsenimi = ik[1]
                    sõnastik[lapsenimi] = vanemanimi
    return(sõnastik)
                