def seosta_lapsed_ja_vanemad(f2, f1):
    fail1 = open(f1, 'r') # nimed.txt
    fail2 = open(f2, 'r') # lapsed.txt
    
    kood_ja_nimi = {}
    laps_ja_vanem = {}
    
    # isikukood:nimi
    for rida in fail1:
        a = rida.split(' ', 1)
        kood = a[0]
        nimi = a[1].strip()
        
        kood_ja_nimi[kood] = nimi
    
    for rida in fail2:               
        b = rida.split()
        vanem = b[0]
        laps = b[1].strip()
        if kood_ja_nimi[laps] in laps_ja_vanem:
            hulk = laps_ja_vanem[kood_ja_nimi[laps]]
            hulk.add(kood_ja_nimi[vanem])
            laps_ja_vanem[kood_ja_nimi[laps]] = hulk
        else:
            hulk = set()
            hulk.add(kood_ja_nimi[vanem])
            laps_ja_vanem[kood_ja_nimi[laps]] = hulk
              
    return laps_ja_vanem

#print(seosta_lapsed_ja_vanemad('nimed.txt', 'lapsed.txt'))
        