def loetleFilmid(zanr):
    f = open("filmid.txt","r",encoding="UTF-8")
    filmid = []
    for line in f.read().splitlines():
        if zanr in line:
            filmid.append(line.split(" - ")[0])
    f.close()
    return filmid
    
def lisaFilm(nimi,zanr):
    f = open("filmid.txt","a",encoding="UTF-8")
    f.write("\n "+nimi+" - "+zanr)
    f.close()
    
def kustutaFilm(nimi):
    f = open("filmid.txt","r",encoding="UTF-8")
    text = f.read().splitlines()
    f.close()
    w = open("filmid.txt","w",encoding="UTF-8")
    for line in text:
        if nimi not in line:
            w.write(line+"\n")
    w.close()