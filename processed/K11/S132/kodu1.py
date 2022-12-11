
def seosta_lapsed_ja_vanemad(lapsed_f, nimed_f):

    vanem_laps_koodid = []
    isikud = []
    d = {}
    
    f = open(lapsed_f)  # Loen failide sisud järjenditesse
    
    for rida in f:
        jupid = rida.split()
        vanem_laps = jupid[0], jupid[1]
        vanem_laps_koodid.append(vanem_laps)
        
    f.close()
    
    f = open(nimed_f, encoding='utf-8')
    
    for rida in f:
        isik = rida.split()
        isik[1] = isik[1] + ' ' + isik[2]
        isik.pop()
        isikud.append(isik)
    
    f.close()
    
    for paar in vanem_laps_koodid:
        
        laps_kood = paar[1]      # Leian lapse nime
        
        for nimi in isikud:
            if laps_kood in nimi:
                laps_nimi = nimi[1]
                
        vanem_kood = paar[0]     # Leian vanema nime
        
        for nimi in isikud:
            if vanem_kood in nimi:
                vanem_nimi = nimi[1]
                
        if laps_nimi not in d.keys():    # Kui last varem sõnastikus polnud, lisan
            d[laps_nimi] = {vanem_nimi}
        
        else:                            # Kui oli, uuendan võtme väärtust
            d[laps_nimi].add(vanem_nimi)
            
    return d

d = seosta_lapsed_ja_vanemad('lapsed.txt', 'nimed.txt')

for laps in d.keys():
    vanemad = ''
    for i in range(len(d[laps])):
        if len(d[laps]) == 1:
            vanemad += d[laps].pop()
        else:
            vanemad += d[laps].pop() + ', '
    print(f'{laps}: {vanemad}')
        
