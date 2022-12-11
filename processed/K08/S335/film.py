def loetleFilmid(a):
    with open("filmid.txt", encoding = "UTF-8") as f:
        filmid = []
        for rida in f:
            rida = rida.split()
            rida = " ".join(rida)
            rida = rida.split(" - ")
            if rida[1] == a:
                filmid += [rida[0]]
    return filmid

def lisaFilm(b, a):
    with open("filmid.txt", "a", encoding = "UTF-8") as f:
        film = " ".join(a) + " - " + "".join(b)
        f.write("\n" + film + "\n")

def kustutaFilm(a):
    with open("filmid.txt", "r", encoding = "UTF-8") as f:
        filmid = f.readlines()
    with open("filmid.txt", "w", encoding = "UTF-8") as f:
        for rida in filmid:
            if not a in rida:
                f.write(rida)