järjend = []

def loetleFilmid(zanr):
    f = open("filmid.txt", "r", encoding="utf-8")
    for rida in f:
        uusrida = rida.strip()
        if zanr in rida and rida not in järjend:
            järjend.append(uusrida)
    return(järjend)


def lisaFilm(nimi, zanr):
    f = open("filmid.txt", "a", encoding="utf-8")
    f.write("\n")
    f.write(nimi,)
    f.write(" - ")
    f.write(zanr)
    f.close()


def kustutaFilm(nimi):
    with open("filmid.txt", "r") as f:
        read = f.readlines()
    with open("filmid.txt", "w") as f:
        for rida in read:
            if not nimi in rida:
                f.write(rida)