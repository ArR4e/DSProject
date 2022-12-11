def loetleFilmid(žanr):
    f = open("filmid.txt", encoding = "UTF-8")
    filmid = []
    for rida in f:
        read = rida.split(" - ")
        read[1] = read[1].strip("\n")
        if read[1] == žanr:
            filmid += [read[0]]
    f.close()
    return filmid

def lisaFilm(nimi, žanr):
    f = open("filmid.txt", "a", encoding = "UTF-8")
    f.write("\n" + nimi + " - " + žanr)
    f.close()
    return

def kustutaFilm(nimi):
    f = open("filmid.txt", encoding = "UTF-8")
    read = f.readlines()
    f.close()
    f = open("filmid.txt", "w", encoding = "UTF-8")
    for i in range(len(read)):
        rida = read[i]
        if rida.split(" - ")[0] == nimi:
            a = 0
        else:
            f.write(rida)
    f.close()
    return
