#lapsed = open('lapsed.txt','r',encoding = 'UTF-8')
#nimed = open('nimed.txt','r',encoding = 'UTF-8')

def seosta_lapsed_ja_vanemad(a,b):
    #loeme sisse vanem-laps paarid ja isikud
    lapsed = open(a,encoding = 'UTF-8')
    nimed = open(b,encoding = 'UTF-8')
    paarid = {}
    for rida in lapsed:
        andmed = rida.strip().split(' ')
        paarid[andmed[0]] = andmed[1] #teeme sõnastiku
    
    isikud = {}
    for rida in nimed:
        andmed = rida.strip().split(' ')
        nimi = ' '.join(andmed[1:])
        isikud[andmed[0]] = nimi #teeme sõnastiku 
    
    lapsed.close()
    nimed.close()
    
    #omistame vanemale lapse nime
    nimed = {}
    for vanem,laps in paarid.items():
        nimed[isikud.get(vanem,0)] = isikud.get(laps,0)

    sõnastik = {}
    for vanem,laps in nimed.items():
        if laps not in sõnastik:
            sõnastik[laps] = set()
            sõnastik[laps].add(vanem)
        if laps in sõnastik:
            sõnastik[laps].add(vanem)
               
    return sõnastik
        
            
seosta_lapsed_ja_vanemad('lapsed.txt','nimed.txt')

#lapsed.close()
#nimed.close()