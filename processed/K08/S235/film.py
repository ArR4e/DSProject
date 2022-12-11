def loetleFilmid(žanr):
    f = open("filmid.txt", "r", encoding = "UTF-8")
    filmid = []
    for rida in f:
        rida = rida.strip().split(" - ")
        nimi = rida[0]
        tüüp = rida[1]
        if tüüp == žanr:
            filmid = filmid + [nimi]
    return filmid


def lisaFilm(nimi, žanr):
    f = open("filmid.txt","a", encoding = "UTF-8")
    f.write('\n' + nimi + " - " + žanr)
    f.close()


def kustutaFilm(nimi):
   f = open("filmid.txt", "r", encoding = "UTF-8")
   read = f.readlines()
   f = open("filmid.txt", "w", encoding = "UTF-8")
   for rida in read:
        rida = rida.strip().split(" - ")
        filmi_nimi = rida[0]
        tüüp = rida[1]
        if filmi_nimi != nimi:
            f.write(filmi_nimi + " - " + tüüp + "\n")
   f.close() 