

def loetleFilmid(zanr):
    f = open("filmid.txt", encoding="utf-8")
    filmid = []
    for film in f:
        if zanr in film:
            jupid = film.split(" - ")
            filmid.append(jupid[0])
          
        
    f.close()
    return filmid

def lisaFilm(nimi, zanr):
    f = open("filmid.txt", mode='a', encoding="utf-8")
    tekst = f"{nimi} - {zanr}"
    f.write("\n" + tekst)
    f.close()

def kustutaFilm(nimi):
    f = open("filmid.txt", mode="r", encoding="utf-8")
    tekst = f.readlines()
    f.close()
    f = open("filmid.txt", mode="w", encoding="utf-8")
    for rida in tekst:
        jupid = rida.split(" - ")
        if nimi == jupid[0]:
            continue
        elif rida == tekst[-1]:
            rida = rida.strip("\n")
            f.write(rida)
        else:
            f.write(rida)
    f.close()

