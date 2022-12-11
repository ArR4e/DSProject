def loetleFilmid(žanr):
    f = open("filmid.txt", "r", encoding = "UTF-8")
    filmid = []
    žanrid = []
    for rida in f:
        jupid = rida.strip().split(" - ")
        nimi = jupid[0]
        žanrinimi = jupid[1]
        žanrid += [žanrinimi]
        if žanrinimi == žanr:
            filmid += [nimi]
    f.close()
    return filmid

def lisaFilm(nimi, žanr):
    f = open("filmid.txt", "a", encoding = "UTF-8")
    f.write("\n" + nimi + " - " + žanr)
    f.close()
    
def kustutaFilm(nimi):
    f = open("filmid.txt", "r", encoding = "UTF-8")
    read = f.readlines()
    f.close()
    f = open("filmid.txt", "w", encoding = "UTF-8")
    kõikread = []
    for rida in read:
        jupid = rida.strip().split(" - ")
        filminimi = jupid[0]
        kõikread += [filminimi]
        if nimi != filminimi:
            f.write(rida)
    if nimi not in kõikread:
        print("Valitud filmi pole.")
    f.close()