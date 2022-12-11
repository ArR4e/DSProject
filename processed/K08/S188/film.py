def loetleFilmid(žanr):
    f = open("filmid.txt", encoding = "utf-8")
    filmid = []
    for rida in f:
        rea_järjend = rida.strip().split(" - ")
        if rea_järjend[1] == žanr:
            filmid = filmid + [rea_järjend[0]]
    f.close()
    return filmid

def lisaFilm(nimi, žanr):
    f = open("filmid.txt", "a", encoding = "utf-8")
    f.write("\n" + nimi + " - " + žanr)
    f.close()

def kustutaFilm(nimi):
    f = open("filmid.txt", "r", encoding = "utf-8")
    sisu = f.readlines()
    f.close()
    f = open("filmid.txt", "w", encoding = "utf-8")
    if len(sisu) >= 2:
        if nimi in sisu[-1]:
            sisu[-2] = (sisu[-2]).strip()
    for rida in sisu:
        if not nimi in rida:
            f.write(rida)
    f.close()
