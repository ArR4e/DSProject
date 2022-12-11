def loetleFilmid(zanr):
    filmid = open("filmid.txt", encoding="UTF-8")
    sobivadfilmid = []
    for rida in filmid:
        filmirida = rida.split(" - ")
        if filmirida[1].strip() == str(zanr):
            sobivadfilmid.append(filmirida[0])
    filmid.close()
    return sobivadfilmid

def lisaFilm(nimi, zanr):
    filmid = open("filmid.txt", "a", encoding="UTF-8")
    filmid.write("\n"+nimi+" - "+str(zanr))
    filmid.close()

def kustutaFilm(nimi):
    filmid = open("filmid.txt", "r", encoding="UTF-8")
    read = filmid.readlines()
    filmid.close()
    filmid_uus = open("filmid.txt", "w", encoding="UTF-8")
    for rida in read:
        if rida.find(nimi) == -1:
            filmid_uus.write(rida)
    filmid_uus.close()
            