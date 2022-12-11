def loetleFilmid(zanr):
    f = open("filmid.txt", encoding="UTF-8")
    filmid = []
    for rida in f:
        if rida == "\n":
            continue
        film = rida.strip().split(' - ')[0]
        zanr1 = rida.strip().split(' - ')[1]
        if zanr == "kõik":
            filmid += [film]
        elif zanr1 == zanr:
            filmid += [film]
    f.close()
    return filmid
        
def lisaFilm(film,zanr):
    f = open("filmid.txt", 'a', encoding="UTF-8")
    f.write("\n" + film + " - " + zanr)
    f.close()
    
def kustutaFilm(film):
    f = open("filmid.txt", encoding="UTF-8")
    read = f.readlines()
    f.close()
    f = open("filmid.txt", "w", encoding="UTF-8")
    for rida in read:
        if rida == "\n":
            continue
        film1 = rida.strip().split(' - ')[0]
        zanr1 = rida.strip().split(' - ')[1]
        if film1 != film:
            f.write(rida)       
    f.close()
