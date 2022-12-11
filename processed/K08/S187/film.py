def loetleFilmid(zanr):
    f = open("filmid.txt", "r")
    filmid = []
    for film in f.readlines():
        film = film.split(" - ")
        if zanr == film[1].strip():
            filmid.append(film[0])
    f.close()
    return(filmid)

def lisaFilm(nimi, zanr):
    f = open("filmid.txt", "a")
    uus_rida = """
""" + " - ".join([nimi, zanr])
    f.write(uus_rida)
    f.close()

def kustutaFilm(nimi):
    f = open("filmid.txt", "r")
    read = f.readlines()
    f.close()

    g = open("filmid.txt", "w")
    for rida in read:
        if nimi not in rida:
            g.write(rida)
    g.close()
