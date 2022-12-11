def seosta_lapsed_ja_vanemad(laste_fail,nimede_fail):
    isikukoodid = open(laste_fail)
    isikukoodid_nimeks = open(nimede_fail)
    nimed = {}
    isikukoodide_sõnastik = {}
    
    for rida in isikukoodid_nimeks:
        andmed = rida.strip().split()
        nimed[andmed[0]] = andmed[1]+ " " + andmed[2]
    isikukoodid_nimeks.close()
    
    for rida in isikukoodid:
        andmed = rida.strip().split()
        if nimed[andmed[1]] not in isikukoodide_sõnastik:
            isikukoodide_sõnastik[nimed[andmed[1]]] = set()
        isikukoodide_sõnastik[nimed[andmed[1]]].add(nimed[andmed[0]])
        
    return isikukoodide_sõnastik
    
sõnastik = seosta_lapsed_ja_vanemad("lapsed.txt","nimed.txt")

for laps in sõnastik:
    sõne = laps + ":"
    for vanem in sõnastik[laps]:
        sõne+=" "+vanem
    print(sõne)
    