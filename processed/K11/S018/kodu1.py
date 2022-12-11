def seosta_lapsed_ja_vanemad(lapsed, nimed):
    
    with open(lapsed, "r", encoding="UTF-8") as f_l:
        jär = f_l.read().split("\n")
        vanemlus = {}
        for i in range(len(jär)):
            jär[i] = jär[i].split()
            vanemad = vanemlus.get(jär[i][1], set())
            vanemad.add(jär[i][0])
            vanemlus[jär[i][1]] = vanemad
    
    with open(nimed, "r", encoding="UTF-8") as f_n:
        jär = f_n.read().split("\n")
        nimed = {}
        for i in range(len(jär)):
            jär[i] = jär[i].split()
            nimi = ""
            for j in range(len(jär[i])-1):
                nimi = nimi + jär[i][j+1] + " "
            nimi = nimi.strip(" ")
            nimed[jär[i][0]] = nimi
        
    vanemdatud = {}
    for laps, vanemad in vanemlus.items():
        for ik in vanemad:
            vanem = vanemdatud.get(nimed[laps], set())
            vanem.add(nimed[ik])
            vanemdatud[nimed[laps]] = vanem
    return vanemdatud

seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt")