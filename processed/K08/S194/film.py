def loetleFilmid(zn): #zn - žanrinimi
    filmilist = []
    zlist = []
    filmidzanrist = []
    with open("filmid.txt") as f0:
        for rida in f0:
            realist = (rida.strip()).split(" - ")
            if zn in realist:
                filmidzanrist += [realist[0]]
    return filmidzanrist
def lisaFilm(nimi, zn):
    with open("filmid.txt", "a") as f1:
        f1.write("\n" +" "+ nimi + " - " + zn)
def kustutaFilm(nimi):
    with open("filmid.txt", "r+") as f2:
        if nimi in f2.readlines():
            f.readlines()[index(nimi)] = f2.write()