def seosta_lapsed_ja_vanemad(flapsed, fnimed):
    fl=open(flapsed)
    fn=open(fnimed)
    loetelu={}
    nimed={}
    #andmed=[]
    for rida in fn:
        andmed=rida.strip().split()
        
        nimi=rida.replace(andmed[0],'').strip()
        
        nimed[andmed[0]]=nimi
    for rida in fl:
        andmed=rida.strip().split()
        if nimed[rida.strip().split()[1]] not in loetelu:
            loetelu[nimed[andmed[1]]]=set()
            loetelu[nimed[andmed[1]]].add(nimed[andmed[0]])
        else:
            loetelu[nimed[andmed[1]]].add(nimed[andmed[0]])
    fl.close()
    fn.close()
    return(loetelu)
loetelu=seosta_lapsed_ja_vanemad('lapsed.txt', 'nimed.txt')
for voti in loetelu:
    print(voti.strip(), end=':')
    i=0
    for el in loetelu[voti]:
        if i<len(loetelu[voti])-1:
            
            print('',el, end=',')
        else:
            print('',el)
        i+=1
    