def loetleFilmid(žanrinimi):
    f = open("filmid.txt", "r", encoding="utf-8")
    filmid = []
    for rida in f:
        eraldi = rida.split(" - ")
        nimi = eraldi[:-1]
        žanr = eraldi[-1].strip()
        if žanrinimi == žanr:
            filmid = filmid + nimi
    f.close()
    return filmid

def lisaFilm(filminimi, žanrinimi):
    f = open("filmid.txt", "a", encoding="utf-8")
    f.write("\n" + filminimi + " - " + žanrinimi)
    f.close()
    return

def kustutaFilm(filminimi):
    f = open("filmid.txt", "r", encoding="utf-8")
    read = f.readlines()
    f.close()

    f2 = open("filmid.txt", "w", encoding="utf-8")
    for rida in read:
        eraldi = rida.split(" - ")
        nimi = eraldi[:-1]
        nimi_sõnena = " ".join(map(str, nimi))
        if filminimi != nimi_sõnena:
            f2.write(rida)
    f2.close()
    return
