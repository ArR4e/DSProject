# Filmide nimekiri

def loetleFilmid(žanr):
    filmid = []
    f = open("filmid.txt", "r", encoding="UTF-8")
    for rida in f:
        if žanr in rida:
            l1 = rida.strip().split(" - ")
            filmid.append(l1[0])
    f.close()
    return filmid

def lisaFilm(nimi, žanr):
    # avab faili et uus film lisada
    f = open("filmid.txt", "a", encoding="UTF-8")
    f.write("\n" + nimi + " - " + žanr)
    f.close()

def kustutaFilm(nimi):
    # loeb failist kõik filmid ja paneb järjendisse
    f = open("filmid.txt", "r", encoding="UTF-8")
    filmid = f.readlines()
    f.close()
    # loob uue faili kuhu lisab kõik filmid peale selle mda kustutada tahetakse
    f = open("filmid.txt", "w", encoding="UTF-8")
    for film in filmid:
        if not nimi in film:
            f.write(film)
    f.close()