def isikukoodid_sõnastikku(fail):
    with open(fail, 'r') as f:
        andmed = f.readlines()
    isikukoodid = dict()
    for rida in andmed:
        jada = rida.strip().split(' ', 1)
        isikukoodid[jada[0]] = jada[1]
    return isikukoodid

def seosta_lapsed_ja_vanemad(lapsed, nimed):
    laste_sõnastik = dict()
    isikukoodid = isikukoodid_sõnastikku(nimed)
    with open(lapsed, 'r') as f:
        laste_koodid = [x.rstrip('\n') for x in f.readlines()]
    for el in laste_koodid:
        koodid = el.split()
        if isikukoodid[koodid[1]] not in laste_sõnastik:
            laste_sõnastik[isikukoodid[koodid[1]]] = {isikukoodid[koodid[0]]}
        else:
            laste_sõnastik[isikukoodid[koodid[1]]].add(isikukoodid[koodid[0]])
    
    return laste_sõnastik
        
andmed = seosta_lapsed_ja_vanemad('lapsed.txt', 'nimed.txt')
for el in andmed:
    print(el, end=': ')
    i = 0
    for vanem in andmed[el]:
        if i == len(andmed[el]) - 1:
            print(vanem, end='\n')
        else:
            print(vanem, end=', ')
        i += 1
