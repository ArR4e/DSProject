def loetleFilmid(zanr):
    filmid = []
    f = open("filmid.txt", encoding = "UTF-8")
    for rida in f:
        rea_osad = rida.strip("\n").split(" - ")
        if rea_osad[1] == zanr :
            filmid = filmid + [rea_osad[0]]
    f.close()
    return(filmid)

def lisaFilm(filminimi, filmizanr):
    f = open("filmid.txt", "a", encoding = "UTF-8")
    f.write("\n" + filminimi + " - " + filmizanr)
    f.close()

    
def kustutaFilm(filminimi):
    f = open("filmid.txt", encoding = "UTF-8")
    fail = f.readlines()
    for rida in fail:
        if filminimi in rida:
            fail.remove(rida)
    f.close()
    f = open("filmid.txt","w",encoding = "UTF-8")
    for el in fail:
        f.write(el)
    f.close()