
def loetleFilmid(žanr):
    with open("filmid.txt", "r") as f:
        filmid = []
        filmilist = []
        for rida in f:
            filmid.append(rida.strip().split(" - "))
        for el in filmid:
            if žanr in el:
                filmilist.append(el[0])
        return filmilist

def lisaFilm(nimi, žanr):
    with open("filmid.txt", "a") as f:
        f.write(f"\n{nimi} - {žanr}")

def kustutaFilm(nimi):
    f = open("filmid.txt", "r")
    filmid = []
    for rida in f:
        filmid.append(rida)             
    f.close()
  
    with open("filmid.txt", "w") as fail:
        for el in filmid:
            if not nimi in el:
                fail.write(el)

