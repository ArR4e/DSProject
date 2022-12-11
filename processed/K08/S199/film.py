def loetleFilmid(zanr):
    f = open("filmid.txt", encoding="UTF-8")
    filmid = []
    for rida in f:
        nimi, genre = rida.strip().split(" - ")
        if genre == zanr:
            filmid.append(nimi)
        else:
            continue
    return(filmid)
    f.close()

def lisaFilm(nimi, zanr):
    f = open("filmid.txt", "a", encoding="UTF-8")
    a = "".join([nimi, " - ", zanr])
    f.write("\n" + a)
    f.close()

def kustutaFilm(nimi):
    f = open("filmid.txt", "r")
    read = f.readlines()
    f = open("filmid.txt", "w")
    for rida in read:
        a = rida.strip().split(" - ")
        if a[0] != nimi:
            f.write(rida)
        else:
            continue
    f.close()


    

