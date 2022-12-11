def seosta_lapsed_ja_vanemad(isikukoodid, nimed):
    sõnastik = {}
    f1 = open(isikukoodid, 'r', encoding='utf8')
    f2 = open(nimed, 'r', encoding='utf8')
    
    for rida in f1:
        koodid = rida.split(' ')
        for rida in f2:
            rida2 = rida.split('')
            if koodid[1] not in sõnastik:
                sõnastik[rida2[1]] = set()
                
                
return sõnastik
                
            
                