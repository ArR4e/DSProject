def loetleFilmid(žanr):
    fail = open("filmid.txt","r+", encoding = "UTF-8")
    filmid = []
    for rida in fail:
        if žanr in rida:
            filmid.append(rida[0: rida.index(žanr) -3])
    fail.close()
    return filmid

def lisaFilm(nimi, žanr):
    fail = open("filmid.txt","a", encoding = "UTF-8")
    fail.write("\n" + nimi+ " - "+ žanr)
    fail.close()
def kustutaFilm(nimi):
    fail = open("filmid.txt","r+", encoding = "UTF-8")
    filmid = []
    filmid += fail.readlines()
    fail = open("filmid.txt","w", encoding = "UTF-8")
    for film in filmid:
        if film.startswith(nimi) == False:
            fail.write(film)
    fail.close()