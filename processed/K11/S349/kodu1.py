def seosta_lapsed_ja_vanemad(lastefailinimi, nimedefailinimi):
    isikukoodid = {}
    with open(lastefailinimi, encoding="UTF-8") as lastefail:
        for rida in lastefail: 
            osad = rida.strip().split(" ")
            vanema_isikukood = osad[0]
            lapse_isikukood=osad[1]
            if vanema_isikukood not in isikukoodid:
                isikukoodid[vanema_isikukood] = []
                isikukoodid[vanema_isikukood].append(lapse_isikukood)
            else:
                isikukoodid[vanema_isikukood].append(lapse_isikukood)
    nimed = {}
    with open(nimedefailinimi, encoding="UTF-8") as nimedefail:
        for rida in nimedefail:
            andmed  = rida.strip().split()
            nimed[andmed[0]]= " ".join(andmed[1:])

    vastus = {} 
    for vanema_isikukood in isikukoodid:
        vanemanimi = nimed[vanema_isikukood]
        lapse_isik = isikukoodid[vanema_isikukood]
        for laps in lapse_isik: 
            lapsenimi = nimed[laps]
            if lapsenimi not in vastus:
                vastus[lapsenimi] = set()
                vastus[lapsenimi].add(vanemanimi)
            elif lapsenimi in vastus:
                vastus[lapsenimi].add(vanemanimi)
    return vastus        
    
print(seosta_lapsed_ja_vanemad("lapsed.txt","nimed.txt"))