def seosta_lapsed_ja_vanemad(lapsed,nimed):
    f = open(lapsed,"r")
    sisu = f.read().replace(" ","\n").split("\n")
    f.close()
    #print(sisu)
    
    vastus = {}
    lisasõnastik = {}
    nimedehulk = set()
    
    f1=open(nimed,"r")
    nimed = f1.read().replace(" ","\n").split("\n")
    f1.close()
    
    
    i = 0 #isikukood
    eesnimi = 1
    perenimi = 2
    while i < len(nimed):
        lisasõnastik[nimed[i]] = (nimed[eesnimi]+" "+nimed[perenimi])
        i += 3
        eesnimi += 3
        perenimi += 3  
    #print(lisasõnastik)
    a = 1
    b = 0
    
    while a < len(sisu):
        if sisu.count(sisu[a]) == 1:
            nimedehulk = set()
        print(sisu.count(sisu[a]))
        if sisu[a] in lisasõnastik:
            nimedehulk.add(lisasõnastik[sisu[b]])
            vastus[lisasõnastik[sisu[a]]] = nimedehulk
        else:
            nimedehulk.add(lisasõnastik[sisu[b]])
            vastus[lisasõnastik[sisu[a]]] = nimedehulk
        #nimedehulk = set()
            #print("Laps ",lisasõnastik[sisu[a]],"vanem",lisasõnastik[sisu[b]])
        a +=2
        b +=2
    return vastus
    
seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt")
