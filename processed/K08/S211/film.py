def loetleFilmid(žanr):
    filmid_fail = open('filmid.txt', 'r')
    
    sisu_jrj = []
    for rida in filmid_fail:
    
        sisu = rida.strip()
    
        sisu_jrj = sisu_jrj + sisu.split(" - ")
    filmid_fail.close()
    otsitavad_filmid = []
    filmide_arv = sisu_jrj.count(žanr)
    
    for i in range(len(sisu_jrj)):
        
        if sisu_jrj[i] == žanr:
            pealkirja_indeks = i - 1
            otsitavad_filmid.append(sisu_jrj[pealkirja_indeks])
    
    return(otsitavad_filmid)

def lisaFilm(nimi, žanr):
    filmid = open('filmid.txt', 'a')
    
    filmid.write('\n')
    filmid.write(nimi)
    filmid.write(" - ")
    filmid.write(žanr)
    
    filmid.close()
    

def kustutaFilm(nimi):
    fail_filmid = open('filmid.txt', 'r')
    
    sisu_jrj=[]
    for rida in fail_filmid:
        sisu = rida.strip()
        sisu_jrj = sisu_jrj + sisu.split(" - ")
    fail_filmid.close()
    
    fail_filmid = open("filmid.txt", "w")
    
    for el in sisu_jrj:
        
        if el == nimi:
            asukoht = sisu_jrj.index(el)
            del sisu_jrj[asukoht]
            del sisu_jrj[asukoht]
            

    for i in range(0, len(sisu_jrj), 2):
        
        fail_filmid.write(" - ".join(sisu_jrj[i:i+2]))
        fail_filmid.write("\n") 

        
        
        
    fail_filmid.close()
  