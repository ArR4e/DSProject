def loetleFilmid(zanr):
    filmid= []
    f = open("filmid.txt", encoding="UTF-8")
    read = f.readlines()
    f.close()
    
    for rida in read:
        rida = rida.strip('\n')
        uusrida= rida.split(" - ")
        if uusrida[-1] == zanr:
            film = uusrida[0]
            filmid.append(film)
    
    return filmid
          
def lisaFilm(nimi, zanr):
    f = open("filmid.txt", "a", encoding="UTF-8")
    f.write("\n" + nimi + " - " + zanr)
    f.close()
    
def kustutaFilm(film):
    a = open("filmid.txt", "r")
    read = a.readlines()
    a.close()
    f = open("filmid.txt", "w")
    for rida in read:
        uusrida= rida.strip("\n").split(" - ")
        if uusrida[0].strip() != film:
            
            f.write(rida)
    f.close()



