def loetleFilmid(žanr):
    filminimed = []
    f = open("filmid.txt", "r")
    for film in f:
        if film == "":
            break
        else:
            film = film.strip().split(" - ")
            if film[-1] == žanr:
                filminimed += [film[0]]
    f.close()
    return filminimed

def lisaFilm(nimi, žanr):
    f = open("filmid.txt", "a")
    f.write("\n " + nimi + " - " + žanr)
    f.close()
    return
    
def kustutaFilm(nimi):
    f1 = open("filmid.txt", "r+")
    read = f1.readlines()
    f2 = open("filmid.txt", "w")
    for film in read:
        if nimi not in film:
            f2.write(film)
    f1.close()
    f2.close()
    return 