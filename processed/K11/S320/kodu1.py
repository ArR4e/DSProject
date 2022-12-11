def seosta_lapsed_ja_vanemad(failinimi1, failinimi2):
    f1=open(failinimi1, "r")
    f2=open(failinimi2, encoding="UTF-8")
    
    sõnastik={}
    lapsevanemad={}
    
    for rida in f2:
        jupid=rida.strip("\n").split(" ",1)
        nimi=jupid[1]
        kood=jupid[0]
        sõnastik[kood]=nimi
        
    #return sõnastik
    
        
    for rida in f1:
        koodid=rida.strip("\n").split(" ")
        vanemakood=koodid[0]
        lapsekood=koodid[1]
        
        if sõnastik[lapsekood] in lapsevanemad.keys():
            
            lapsevanemad[sõnastik[lapsekood]].add(sõnastik[vanemakood])
        
        else:
            lapsevanemad[sõnastik[lapsekood]]={sõnastik[vanemakood]}
            
            
    f1.close()
    f2.close()
    
    return lapsevanemad
    
seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt")

