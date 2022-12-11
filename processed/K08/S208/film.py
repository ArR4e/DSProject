def loetleFilmid(žanr):
    f = open("filmid.txt")
    tag = []
    for rida in f:
        jrj = rida.strip().split(" - ")
        film = jrj[0]
        if žanr == jrj[1]:
            tag.append(film)
    f.close()
    return tag
def lisaFilm(nimi, žanr):
    f = open("filmid.txt", "a+")
    f.write( "\n" +nimi+" - "+žanr)
    f.close()
def kustutaFilm(nimi):
    f = open("filmid.txt", "r")
    read = f.readlines()
    f.close()
    f2 = open("filmid.txt", "w+")
    for rida in read:
        jrj = rida.strip().split(" - ")
        if jrj[0] != nimi:
            f2.write(rida)
    f2.close()
            