def loetleFilmid(zanr):
    fail=open("filmid.txt", "r", encoding="utf-8")
    faili_sisu=[]
    for rida in fail:
        osad=rida.split(" - ")
        for osa in osad:
            faili_sisu.append(osa.strip("\n"))
            
    zanrid=[]
    filmid=[]
    i=1
    while i<len(faili_sisu):
        filmid.append(faili_sisu[i-1])
        zanrid.append(faili_sisu[i])
        i+=2
    a=0
    vastus=[]
    for el in zanrid:
        if zanr==el:
            indeks=[i for i, n in enumerate(zanrid) if n==zanr][a]
            vastus.append(filmid[indeks])
            a+=1
            continue
        else:
            continue
    fail.close()
    return vastus
    
    

def lisaFilm(nimi,zanr):
    fail=open("filmid.txt", "a+", encoding="utf-8")
    lisame=(str(nimi) + " - " + str(zanr))
    fail.write("\n")
    fail.write(lisame)
    fail.close()
    return True
    
    
    
def kustutaFilm(nimi):
    fail=open("filmid.txt", "r", encoding="utf-8")
    faili_sisu=[]
    for rida in fail:
        osad=rida.split(" - ")
        for osa in osad:
            faili_sisu.append(osa.strip("\n"))
    fail.close()    
    zanrid=[]
    filmid=[]
    i=1
    while i<len(faili_sisu):
        filmid.append(faili_sisu[i-1])
        zanrid.append(faili_sisu[i])
        i+=2
    for el in filmid:
        if el==nimi:
            indeks=filmid.index(nimi)
            del filmid[indeks]
            del zanrid[indeks]
        else:
            continue
    fail=open("filmid.txt", "w", encoding="utf-8")
    a=0
    for a in range(len(filmid)):
        fail.write(filmid[a])
        fail.write(" - ")
        fail.write(zanrid[a])
        fail.write("\n")
        a+=1
    fail.close()
    return True
