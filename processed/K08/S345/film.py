def loetleFilmid(žanr):
    f = open("filmid.txt", encoding="UTF-8")
    järjend = []
    for rida in f:
        film = rida.strip().split(" - ")
        if žanr in film:
            järjend.append(film[0])
    f.close()
    return järjend

def lisaFilm(nimi, žanr):
    f = open("filmid.txt", "a", encoding="UTF=8")
    f.write("\n" + nimi + " - " + žanr)
    f.close()

def kustutaFilm(nimi):
    f = open("filmid.txt", "r", encoding="UTF-8")
    filmid = f.read().split("\n")
    f.close()
    
    f = open("filmid.txt", "w", encoding="UTF-8")
    for film in filmid:
        if nimi in film:
            continue
        else:
            f.write(film + "\n")
    f.close()