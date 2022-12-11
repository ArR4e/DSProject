def faili_avamine(nimi):
    f = open(nimi, 'r', encoding = 'UTF-8')
    nimekiri = []
    for a in f:
        a = a.strip().split()
        nimekiri.append(a)
    return nimekiri



def seosta_lapsed_ja_vanemad(lapsed, nimed):
    pere = {}
    f_lapsed = faili_avamine(lapsed)
    f_nimed = faili_avamine(nimed)
    print(f_lapsed)
    print(f_nimed)
    for a in f_lapsed:
        
        x = []
        if a[1] in pere.keys():
            n = pere.get(a[1])
            x.append(a[0])
            x.append(n)
            pere[a[1]] = x
        else:
            pere[a[1]] = a[0]
        
    print(pere)
    
    
    for z in pere:
        print(z)
        for p in f_nimed:
            h = p
            print(p)
            if z == p[0]:
                h.remove(h[0])
                #print(str(z) + ' ' + str(h))
                pere[str(h)] = pere.pop(z)
            
    print(pere)
        
        
        #ollus = pere.get(z)
        
    
    
seosta_lapsed_ja_vanemad('lapsed.txt', 'nimed.txt')