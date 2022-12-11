
def loetleFilmid(žanr):
    film = []
    fail = open("filmid.txt", "r", encoding = "utf-8")
    film = fail.readline()
    for rida in fail:
        jaotus = rida.split(" - ")
        nimetus = jaotus[0]
        filmizanr = ((a[1].split("\n"))[0])
        if filmizanr == žanr:
            film.append(nimi)      
    fail.close
    return film


def lisaFilm(nimi, žanr):
    fail = open("filmid.txt", "w", encoding = "utf-8")
    filmkooszanriga = nimi + " - " + žanr
    fail.writelines("n" + filmkooszanriga)
    fail.close
    
def kustutaFilm(nimi):
    fail = open("filmid.txt", "w", encoding = "utf-8")
    fail.readlines()
    fali.close
    newfile = open("filmid.txt", "w", encoding = "utf-8")
    for line in newfile:
        
        
    
    