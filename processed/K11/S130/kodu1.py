f = open('lapsed.txt')
n = open('nimed.txt', encoding = 'utf-8')

def seosta_lapsed_ja_vanemad(f, n):
       
    d = {}
    lopp = {}
    for rida in n:
        c = rida.strip().split(' ',1)
        d[c[0]] = c[1]
        
#d on isikukoodide : nimede sonastik
#a on ridade kaupa info failist, kus esimesel kohal vanema isikukood ja teisel kohal lapse isikukood.
    
    for rida in f:
        a = rida.strip().split()
        voti = a[1]
        vaartus = a[0]
        if voti in d:
            if voti not in lopp:
                lopp[d[voti]] = set()
        if vaartus in d:
            if d[vaartus] not in lopp:
                lopp[d[voti]].add(d[vaartus])
            else:
                lopp[d[voti]].add(d[vaartus])
                #Siin peaks teise vanema juurde lisama minu idee poolest, aga ta ei tee seda.
            
    print(lopp)

print(seosta_lapsed_ja_vanemad(f,n))
#Mul arvutis see programm tootab, ainus asi on, et ta ei margi ara kahte vanemat

    
f.close()
n.close()