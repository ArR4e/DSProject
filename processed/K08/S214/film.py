def loetleFilmid(žanr):
    f = open("filmid.txt","r",encoding = "utf-8")
    filmide_nimed = []
    for rida in f:
        if rida.strip().endswith(žanr):
            film = rida.split(" -")
            film = film[0]
            filmide_nimed += [film]
    f.close()
    return filmide_nimed

def lisaFilm(nimi,žanr):
    f = open("filmid.txt","a+",encoding = "utf-8")
    f.write("\n"+str(nimi)+" - "+žanr)
    f.close()

def kustutaFilm(nimi):
    f = open("filmid.txt","r", encoding = "utf-8")
    read = []
    for rida in f:
        if rida.startswith(nimi):
            read = read
        else:
            read += [rida]
    f.close()
    f = open("filmid.txt","w", encoding = "utf-8")
    for el in read:
        f.write(str(el))
    