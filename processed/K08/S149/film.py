def loetleFilmid(žanr):
    with open("filmid.txt", encoding = "UTF-8") as f:
        filmid = f.readlines() 
    žanriFilmid = [film.strip().split(" - ")[0] for film in filmid if žanr in film.strip()]
    return žanriFilmid

def lisaFilm(nimi, žanr):
    with open("filmid.txt", "r", encoding = "UTF-8") as r:
        if r.readlines() != []:
            lines = True
        else:
            lines = False
    with open("filmid.txt", "a+", encoding = "UTF-8") as f:
        if lines:
            f.write("\n")
        f.write(nimi + " - " + žanr)

def kustutaFilm(nimi):
    with open("filmid.txt", encoding = "UTF-8") as r:
        filmid = r.readlines()
    with open("filmid.txt", "w+", encoding = "UTF-8") as f:
        for film in filmid:
            if nimi not in film.split(" - "):
                f.write(film)

print(loetleFilmid("seiklus"))