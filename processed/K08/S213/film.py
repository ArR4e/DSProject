def loetleFilmid(zanr):
    
    filmid = []
    f = open("filmid.txt", "r", encoding = "UTF-8")
    
    for rida in f:
        if zanr in rida:
            filmid.append(rida[0: rida.index(zanr) - 3])
            
    f.close()
    return filmid
    
def lisaFilm(nimi, zanr):
    
    f = open("filmid.txt", "a", encoding = "UTF-8")
    f.write("\n" + nimi + " - " + zanr)
    
    f.close()
    
def kustutaFilm(nimi):
    
    f = open("filmid.txt", "r", encoding = "UTF-8")
    filminimed = []
    
    for rida in f:
        filminimed.append(rida)
    
    f.close()
    f = open("filmid.txt", "w", encoding = "UTF-8")
        
    for film in filminimed:
        if nimi not in film:
            f.write(film)
    
    f.close()
