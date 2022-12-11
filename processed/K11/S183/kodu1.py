def seosta_lapsed_ja_vanemad(laps, nimi):
    vanema_sõnastik = {}
    lapse_sõnastik = {}
    laps_isik = []
    vanema_isik = []
    uus_vana = {}
    uus_laps = {}
    pere ={}
    with open("lapsed.txt", encoding = "UTF-8") as lapsed:
        for i in lapsed:
            vanem_laps_isik1 = i.strip("\n")
            vanem_laps_isik2 = vanem_laps_isik1.split(" ")
            vanema_sõnastik = vanem_laps_isik2[0]
            vanema_isik += [vanema_sõnastik]
            lapse_sõnastik = vanem_laps_isik2[1]
            laps_isik += [lapse_sõnastik]
    with open("nimed.txt", encoding = "UTF-8") as nimed:
        for j in nimed:
            isik_ja_nimi1 = j.strip("\n")
            isik_ja_nimi2 = isik_ja_nimi1.split(" ", 1)
            isikukood = isik_ja_nimi2[0]
            Ees_ja_perekonnanimi = isik_ja_nimi2[1]
            if isikukood in vanema_isik:
                uus_vana[isikukood] = Ees_ja_perekonnanimi
            else:
                pass
            if isikukood in laps_isik:
                uus_laps[isikukood] = Ees_ja_perekonnanimi
            else:
                pass
        for k in range(len(laps_isik)):
            try:
                if uus_laps[laps_isik[k]] in pere.keys():
                    pere[uus_laps[laps_isik[k]]] += [uus_vana[vanema_isik[k]]]
                    
                else:
                    pere[uus_laps[laps_isik[k]]] = [uus_vana[vanema_isik[k]]]
            except:
                pass
        lapsi = []
        lapsi +=pere.keys()
        for q in range(len(lapsi)):
            pere[uus_laps[laps_isik[q]]] = set(pere[uus_laps[laps_isik[q]]])
        return pere
            
lõpp = seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt")
segu = []
segu += lõpp.keys()
segu2 = []
segu2 += lõpp.values()
for a in range(len(lõpp)):
    kao = ""
    kao = str(segu2[a])
    kao = kao.strip("{")
    kao = kao.strip("}")
    kao = kao.strip("'")
    kao = kao.replace("', '", ", ")
    kao = kao.strip("['")
    kao = kao.strip("']")
    print(str(segu[a]) +": " + kao)          
    