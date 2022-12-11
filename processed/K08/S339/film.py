def loetleFilmid(žanrinimi):
    f = open("filmid.txt", encoding = "utf-8")
    filmid = []
    for rida in f:
        if žanrinimi in rida:
            rida = rida.split(" - ")
            filmid.append(rida)
        f.close()
        return(filmid)
            
def lisaFilm(nimi,žanr):
    f = open("filmid.txt", "a", encoding = "utf-8")
    nimi = nimi.capitalize()
    žanr = žanr.lower()
    uus = (nimi + " - " + žanr)
    f.write(uus + "\n")
    f.close()
    return(uus)
    
def kustutaFilm(filminimi):
    lines = []
    with open("filmid.txt", "r", encoding = "utf-8") as f:
        lines = f.readlines()
    with open("filmid.txt", "w", encoding = "utf-8") as f:
        filminimi = filminimi.capitalize()
        for line in lines:
            if filminimi not in line:
                f.write(line)