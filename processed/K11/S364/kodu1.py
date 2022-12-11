def seosta_lapsed_ja_vanemad(f1, f2):
    fail = open(f1, 'r')
    dictionary = {}
    
    for rida1 in fail:
        rida1 = rida1.strip().split()
        vanem_kood = rida1[0]
        lapse_kood = rida1[1]
        fail2 = open(f2, 'r')
        
        for rida2 in fail2:
            rida2 = rida2.strip().split()
            kood = rida2[0]
            nimi = ' '.join(rida2[1:])
            if vanem_kood == kood:
                x = nimi
            elif lapse_kood == kood:
                y = nimi
                
        dictionary.setdefault(x, []).append(y)
    fail2.close()
        
    for el in dictionary:
        a = set(dictionary[el])
        dictionary[el] = a
    fail.close()
    return dictionary




