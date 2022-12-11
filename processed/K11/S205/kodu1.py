def seosta_lapsed_ja_vanemad(lastefail, nimedefail):
    f = open(lastefail, 'r', encoding='utf-8')
    f2= open(nimedefail,'r', encoding='utf-8')
    isikud = {}
    laps_vanem = {}
    
    
    for rida in f2:
        isik = [rida.strip()[:11], rida.strip()[12:]]
        isikud[isik[0]]=isik[1]
    for rida in f:
        tühi = set()
        kombo = rida.strip().split(' ')
        vanem = isikud[kombo[0]]
        if isikud[kombo[1]] not in laps_vanem:
            laps_vanem[isikud[kombo[1]]]=set()
        laps_vanem.get(isikud[kombo[1]]).add(vanem)
            
                
                
    f.close()
    f2.close()
    return laps_vanem
            

print(seosta_lapsed_ja_vanemad('lapsed.txt','nimed.txt'))