def seosta_lapsed_ja_vanemad(f,g):
    f = open("lapsed.txt")
    g = open("nimed.txt")
    vanemad = {}
    for rida in f:
        rida = rida.split()
        if rida[1] in vanemad.keys():
            vanemad[rida[1]] = (vanemad[rida[1]], rida[0])
        else:
            vanemad[rida[1]] = rida[0]
    lapsed = {}
    for rida in g:
        rida = rida.split()
        lapsed[rida[0]] = rida[1] + " " + rida[2]
    tulemus = {}
    for l,v in vanemad.items():
        laps_nimi = lapsed[l]
        vanemate_nimed = set()
        if len(v) == 11:
            x = lapsed[v]
            vanemate_nimed.add(x)
        else:
            van1,van2 = v
            vanemate_nimed.add(lapsed[van1])
            vanemate_nimed.add(lapsed[van2])
        tulemus[laps_nimi] = vanemate_nimed          
    return tulemus
