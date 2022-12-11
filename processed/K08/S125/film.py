def loetleFilmid(žanr):
    f = open("filmid.txt", encoding="UTF-8")
    filmid = []
    for rida in f:
        järjend = rida.strip().split(" - ")
        if järjend[1] == žanr:
            filmid.append(järjend[0])
    f.close()
    return filmid

def lisaFilm(film, žanr):
    f = open("filmid.txt", "a", encoding="UTF-8")
    f.write("\n" + film + " - " + žanr)
    f.close()
    
def kustutaFilm(film):
    f = open("filmid.txt", encoding="UTF-8")
    read = f.readlines()
    f.close()
    
    f1 = open("filmid.txt", "w", encoding="UTF-8")
    for rida in read:
        if film not in rida:
            f1.write(rida)
    f1.close()