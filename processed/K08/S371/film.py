def loetleFilmid(filmi_žanr):
    andmed = []
    nimed = []
    žanrid = []
    kordus = 0
    i = 0

    fail = open("filmid.txt", encoding = "UTF-8")
    for rida in fail:
        andmed.append(rida.strip().split(" - "))
        nimi = andmed[i][0]
        žanr = andmed[i][1]
        kordus += 1
        nimed.append(nimi)
        žanrid.append(žanr)
        i += 1
        
    fail.close()

    filmid = []
    a = 0
    
    while kordus > 0:
        if filmi_žanr == žanrid[a]:
            filmid.append(nimed[a].strip())
            a += 1
            kordus -= 1
        else:
            a += 1
            kordus -=1
    return filmid
    
def lisaFilm(pealkiri, žanr):
    fail = open("filmid.txt", "a+", encoding = "UTF-8")
    fail.write("\n")
    fail.write(pealkiri + " - " + žanr)
    fail.close()
    
def kustutaFilm(pealkiri):
    andmed = []
    read = []
    nimed = []
    i = 0
    kordus = 0
    
    fail = open("filmid.txt", encoding = "UTF-8")
    for rida in fail:
        read.append(rida.strip())
        andmed.append(rida.strip().split(" - "))
        nimi = andmed[i][0]
        nimed.append(nimi)
        i += 1
        kordus += 1
    fail.close()
    
    a = 0
    fail = open("filmid.txt", "w", encoding = "UTF-8")
    while kordus > 0:
        if nimed[a] != pealkiri:
            fail.write(read[a])
            fail.write("\n")
            a += 1
            kordus -= 1
        else:
            a += 1
            kordus -= 1
                
    fail.close()
            
loetleFilmid("märul")
         
