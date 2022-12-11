
def seosta_lapsed_ja_vanemad(fail1, fail2):
    
    laps_ja_vanemate_IDd = {}
    with open(fail1, 'r', encoding='UTF-8') as f1:
        for rida in f1:
            info_järjendina = rida.strip().split()
            if info_järjendina[1] not in laps_ja_vanemate_IDd.keys():
                laps_ja_vanemate_IDd[info_järjendina[1]]= set([info_järjendina[0]])
            else:
                laps_ja_vanemate_IDd[info_järjendina[1]].add(info_järjendina[0])
            
    ID_ja_nimi = {}
    with open(fail2, 'r', encoding='UTF-8') as f2:
        for rida in f2:
            info_järjendina2 = rida.strip().split()
            ID_ja_nimi[info_järjendina2[0]] = ' '.join(info_järjendina2[1:])
            
    tulemus = {}
    for lapseid, vanemaid in laps_ja_vanemate_IDd.items():
        vanemate_nimed = []
        for ID in list(laps_ja_vanemate_IDd[lapseid]):
            vanemate_nimed.append(ID_ja_nimi[ID])
        tulemus[ID_ja_nimi[lapseid]] = set(vanemate_nimed)
    
    return tulemus
for laps, vanemad in list(seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt").items()):
    print(laps+':', ', '.join(list(vanemad)))
    

