def loetleFilmid(zanr):
    f = open("filmid.txt", encoding = "UTF=8")
    sobivad_filmid = []
    for el in f:
        if zanr in el:
            tühikuta = el.lstrip()
            reata = tühikuta.strip()
            sobivad_filmid.append(reata)
    f.close()
    filmide_list = []
    for el in sobivad_filmid:
        nimi = (el.split(" - ")[0])
        filmide_list.append(nimi)
    return filmide_list

def lisaFilm(nimi, zanr):
    f = open("filmid.txt", encoding="UTF-8", mode="r+")
    sisu = f.readlines()
    f.write("\n" + " " + nimi + " - " + zanr)
    f.close()
    return 

def kustutaFilm(nimi):
    f = open("filmid.txt", encoding="UTF-8", mode="r+")
    sisu = f.readlines()
    for el in sisu:
        if nimi in el:
            sisu.remove(el)
    f.truncate(0)
    f.write("".join([str(el) for el in sisu]))
    f.close()
    return