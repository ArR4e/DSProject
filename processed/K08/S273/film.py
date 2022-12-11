def loetleFilmid(žanr):
    f = open("filmid.txt", encoding="utf-8")
    sisu = f.readlines()
    filmid = []
    for film in sisu:
        a = film.split(" - ")
        if a[1].strip() == žanr:
            filmid.append(a[0])
    f.close()
    return filmid

#loetleFilmid("multikas")

def lisaFilm(nimi,žanr):
    f = open("filmid.txt", "a", encoding="utf-8")
    f.write("\n" + nimi + " - " + žanr + "\n")
    f.close()
    print("Film lisatud!")  

#lisaFilm("Avengers: Endgame","märul")

def kustutaFilm(film):
    f = open("filmid.txt", "w+", encoding="utf-8")
    read = f.readlines()
    n = 0
    for film in read:
        fz = film.split(" - ")
        if fz[0] == film:
            del read[n]
        n += 1
    f.write(str(read))
    print("Tehtud")
    f.close()

#kustutaFilm("Moana")