def loetleFilmid(zanr):
    f = open("filmid.txt", encoding = "UTF-8")
    nimed = []
    for line in f:
        line = line.split(" - ")
        fnimi = line[0]
        fzanr = line[1].strip()
        if zanr == fzanr:
            fnimi = [fnimi]
            nimed = nimed + fnimi
    f.close()
    return nimed


def lisaFilm(nimi, zanr):
    f = open("filmid.txt", "r+", encoding = "UTF-8")
    while True:
        read = f.readline()
        if read == "":
            f.write("\n"+ nimi + " - " + zanr)
            f.close()
            break


def kustutaFilm(nimi):
    f1 = open("filmid.txt", "r+", encoding = "UTF-8")
    read = f1.readlines()
    f1.close()
    while True:
        f2 = open("filmid.txt", "w", encoding = "UTF-8")
        for line in read:
            sõna = line.split(" - ")
            fnimi = sõna[0]
            if fnimi != nimi:
                f2.write(line)
        return