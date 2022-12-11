sõnastik = {}
sõna = {}
final = set()
ku = set()
be = set()

fail = open ("lapsed.txt", encoding = "UTF-8")
fail2 = open ("nimed.txt", encoding = "UTF-8")

def seosta_lapsed_ja_vanemad(fail, fail2):

    for rida in fail:
        vanem, laps = rida.strip().split(" ")
        sõnastik[laps] = vanem
    for rida in fail2:
        isikukood, lnimi, lpere = rida.strip().split(" ")
        sõna[isikukood]=lnimi+" "+lpere

    for el in sõna:
    
        if el in sõnastik:
            final.add(el+": "+sõnastik[el])
        #final.add(sõnastik[el])
        else:
            final.add(el)
    for el in final:
        u=el.split(": ")
        if u[0] in sõnastik:
            nel=sõna[u[0]]
            el=nel
            if len(u)>1:
                ku.add(nel+": "+u[1])
            else:
                ku.add(nel)
        else:
            ku.add(sõna[u[0]])
    for el in ku:
        q=el.split(": ")
        if len(q)>1:
            if q[1] in sõna:
                pel=sõna[q[1]]
            el=pel
            be.add(q[0] + ": " + pel)
        else:
            be.add(q[0])
    
    
# print(final)
#print(ku)
    return be
        
    
    #if el in sõnastik:
        
        
        
        
            
    
    
    
    
    
#print (sõnastik)
#print (sõna)