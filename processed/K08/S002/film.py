def loetleFilmid(zanr):
    fail = open("filmid.txt","r",encoding="utf-8")
    tekst = fail.readlines()
    fail.close()
    film = []
    for i in tekst:
        if i.split(" - ")[-1].strip("\n") == zanr:
            film.append(i.split(" - ")[0])
    return film

def lisaFilm(nimi,zanr):
    fail = open("filmid.txt","a",encoding="utf-8")
    fail.write("\n"+nimi+" - "+zanr)
    fail.close()
    
    
def kustutaFilm(nimi):
    fail = open("filmid.txt","r",encoding="utf-8")
    tekst = fail.readlines()
    fail = open("filmid.txt","w",encoding="utf-8")
    for i in tekst:
        if i.split(" - ")[0] != nimi:
            fail.write(i)
    fail.close()