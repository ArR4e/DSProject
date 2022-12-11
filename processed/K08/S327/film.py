def loetleFilmid(zanr):
    f = open("filmid.txt", encoding = "UTF-8")
    filmid = []
    for rida in f:
        if zanr in rida:
            filmid.append(rida.split(" - ")[0])
    f.close()
    return filmid

def lisaFilm(nimi, zanr):
    f = open("filmid.txt","a", encoding = "UTF-8")
    f.write("\n " + nimi + " - " + zanr)
    f.close()

def kustutaFilm(nimi):
    f = open("filmid.txt", encoding = "UTF-8")
    read = f.readlines()
    f.close()
    f2 = open("filmid.txt","w", encoding = "UTF-8")
    for rida in read:
        if nimi in rida:
            continue
        else:
            f2.write(rida)
    f2.close()