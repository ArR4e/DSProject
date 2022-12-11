def seosta_lapsed_ja_vanemad(laste_fail, nimede_fail):
    isikukood_to_nimed = {}
    with open(nimede_fail, 'r', encoding='UTF-8') as f:
        for line in f:
            andmed = line.strip().split(maxsplit=1)
            
            isikukood_to_nimed[andmed[0]] = andmed[1]
            
    lapsed_vanemad = {}
    
    with open(laste_fail, 'r', encoding='UTF-8') as f:
        for line in f:
            andmed = line.strip().split()
            if isikukood_to_nimed[andmed[1]] in lapsed_vanemad:
                lapsed_vanemad[isikukood_to_nimed[andmed[1]]].add(isikukood_to_nimed[andmed[0]])
            else:
                lapsed_vanemad[isikukood_to_nimed[andmed[1]]] = {isikukood_to_nimed[andmed[0]]}
                
    return lapsed_vanemad

d = seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt")
for key in d:
    print(key, ': ', end='', sep='')
    print(*d[key], sep=', ')