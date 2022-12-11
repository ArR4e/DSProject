def loetleFilmid(zanr):
    f = open("filmid.txt", "r", encoding = "UTF-8")
    filmid = []
    for i in f:
        rida = i.split(" - ")
        film = rida[0].strip()
        klass = rida[1].strip()
        
        if klass == zanr:
            filmid.append(film)
    
    return filmid

def lisaFilm(nimi, zanr):
    f = open("filmid.txt", "a", encoding = "UTF-8")
    f.write("\n" + nimi + " - " + zanr)
    f.close()
    
    
def kustutaFilm(kustuta):
    f = open("filmid.txt", "r", encoding = "UTF-8")
    filmid = []
    kustuta = kustuta.strip()
    for i in f:
        rida = i.split(" - ")
        film = rida[0].strip()
        
        if film != kustuta:
            filmid.append(i)
            
    f.close()
    f = open("filmid.txt", "w", encoding = "UTF-8")
            
    for i in filmid:
        f.write(i)
    f.close()