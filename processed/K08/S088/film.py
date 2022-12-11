def loetleFilmid(a):
    f = open("filmid.txt", encoding = "UTF-8")
    fl = []
    for i in f:
        if a in i:
            film = i.split(" - ")[0]
            fl.append(film.strip())
    return fl
    f.close()

def lisaFilm(n, z):
    f = open("filmid.txt", "a", encoding = "UTF-8")
    a = "\n" + n + " - " + z
    f.write(a)
    f.close()

def kustutaFilm(a):
    f = open("filmid.txt", "r", encoding = "UTF-8")
    sisu = f.readlines()
    for i in sisu:
        if a in i:
            sisu.remove(i)
    f.close()
    
    f = open("filmid.txt", "w", encoding = "UTF-8")
    for i in sisu:
        f.write(i)
    f.close()