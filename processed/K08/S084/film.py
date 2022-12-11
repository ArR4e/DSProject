def loetleFilmid(zanr):
    vahekoht = " - "
    filmid = []
    with open("filmid.txt", encoding="UTF-8") as f:
        for line in f.readlines():
            if line.count(zanr)>0:
                filmid.append(line[0:line.index(vahekoht)])
    return filmid
def lisaFilm(nimi, zanr):
    with open("filmid.txt", "a",encoding="UTF-8") as f:
        f.write("\n"+nimi+" - "+zanr)
def kustutaFilm(nimi):
    tekst = ""
    with open("filmid.txt", encoding="UTF-8") as f:
        for line in f.readlines():
            if line.count(nimi)==0:
                tekst+=line
    with open("filmid.txt","w", encoding="UTF-8") as f:
        f.write(tekst)