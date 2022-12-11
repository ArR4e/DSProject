def seosta_lapsed_ja_vanemad(fail1, fail2):
    vanem_laps = {} #laps : vanem1, vanem2
    nimed = {}      #isikukood: "nimi"
    with open(fail1, "r") as fail1, open(fail2, "r") as fail2:
        for line in fail1:
            vanem, laps = line.strip().split(" ")
            if laps in vanem_laps:
                vanem_laps[laps] = vanem_laps[laps] + ", " +vanem
            else:
                vanem_laps[laps] = vanem
            
        for line in fail2:
            idkood, eesnimi, perenimi = line.strip().split(" ")
            nimed[idkood] = eesnimi + " " + perenimi
    
    tulemus_sõnastik = {}
    for lapsenimi in vanem_laps:
        if not lapsenimi in tulemus_sõnastik:
            vanem1 = 0
            vanem2 = 0
            lapse_nimi = nimed[lapsenimi]
            tulemus_sõnastik[lapse_nimi] = set()
            try:
                vanem1, vanem2 = vanem_laps[lapsenimi].split(", ")
                vanem1 = nimed[vanem1]
                vanem2 = nimed[vanem2]
                tulemus_sõnastik[lapse_nimi].add(vanem1 + ", " + vanem2)
            except:
                vanem1 = nimed[vanem_laps[lapsenimi]]
                tulemus_sõnastik[lapse_nimi].add(vanem1)
            
        else:
            print("error")
            
    return(tulemus_sõnastik)

kole_vastus = seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt")
            
for i in kole_vastus:
    print (i + ": " + str(kole_vastus[i]))
#print(seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt"))