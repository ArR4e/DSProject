def seosta_lapsed_ja_vanemad(lastenimede_algfail,nimede_algfail):
    # isikukoodide ja nimede dictonary loomine
    spikker = dict()
    kõigi_isikukoodid = []
    nimed = []
    fail_nimed = open(nimede_algfail)
    for rida in fail_nimed:
        järj = rida.split(" ",1)
        spikker[järj[0]] = (järj[1]).strip()
    
    # nimede dictionary loomine
    lapsed_vanemad = dict()
    fail_isikukoodid = open(lastenimede_algfail)
    for rida in fail_isikukoodid:
        järjend = rida.split(" ",1)
        lapse_nimi = spikker[(järjend[1]).strip()]
        vanema_nimi = spikker[järjend[0]]
        if lapse_nimi not in lapsed_vanemad:
            lapsed_vanemad[lapse_nimi] = {vanema_nimi}
        else:
            vanemate_nimed = lapsed_vanemad[lapse_nimi]
            vanemate_nimed.add(vanema_nimi)
    
    return lapsed_vanemad

print(seosta_lapsed_ja_vanemad("lapsed.txt","nimed.txt"))