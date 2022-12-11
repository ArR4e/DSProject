import os

def loetleFilmid(zanr):
    filmid = []
    loetelu = []
    fail = open("filmid.txt", "r+", encoding="utf-8")
    for rida in fail:
        realt = rida.strip().split(" - ")
        filmid.append(realt)
    for film in filmid:
        for el in film:
            if el == zanr:
                loetelu.append(film[0])
    fail.close()
    if not loetelu:
        return []
    else:
        return loetelu

def lisaFilm(nimi, zanr):
    f = open("filmid.txt", "a", encoding="utf-8")
    sõne = nimi + " - " + zanr
    f.write("\n" + sõne)
    f.close()

def kustutaFilm(filminimi):
    filminimi1 = filminimi.split(" - ")
    filmid = []
    fail = open("filmid.txt", "r", encoding="utf-8")
    for rida in fail:
        realt = rida.strip().split(" - ")
        filmid.append(realt)
    for film in filmid:
        if filminimi1 == film or filminimi1[0] == film[0]:
            filmid.remove(film)
    fail.close()
    fail1 = open("filmid.txt", "w", encoding="utf-8")
    for f in filmid:
        sõne = f[0] + " - " + f[1]
        fail1.write(sõne + "\n")
    fail1.close()
    

