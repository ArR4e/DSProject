def loetleFilmid(zanr):
    tagasta = []
    f = open("filmid.txt",encoding="UTF-8")
    for rida in f:
        ri = rida.strip("\n")
        r = ri.split(" - ")
        if r[1] == zanr:
            tagasta += [r[0]] 
    return(tagasta)
def lisaFilm(nimi, zanr):
    f = open("filmid.txt", "a",encoding="UTF-8")
    uusrida=("\n"+nimi+" - "+zanr)
    f.write(uusrida)
    return
def kustutaFilm(nimi):
    f = open("filmid.txt", "r", encoding="UTF-8")
    read = f.readlines()
    i = 0
    for rida in read:
        ri = rida.strip("\n")
        r = ri.split(" - ")
        if r[0] == nimi:
            del read[i]
        i += 1
    f.close()
    f = open("filmid.txt", "w+", encoding="UTF-8")
    for rida in read:
        f.write(rida)
    return
