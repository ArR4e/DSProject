
def loetleFilmid(žanrinimi):
    filmifail = open("filmid.txt", "r+", encoding="UTF=8")
    b = []
    for rida in filmifail:
        a = rida.split(" - ")
        filminimi = a[0]
        žanrinimi1 = a[1].strip()
        if žanrinimi == str(žanrinimi1):
            b.append(filminimi)
    return b
    filmifail.close()

def lisaFilm(nimi, žanr):
    filmifail = open("filmid.txt", "a", encoding="UTF=8")
    filmifail.writelines("\n" + nimi + " - " + žanr)
    filmifail.close()
    
def kustutaFilm(filminimi):
    f = open("filmid.txt")
    väljund = []
    for rida in f:
        if filminimi not in rida:
            väljund.append(rida)
    f.close
    f = open("filmid.txt", "w")
    f.writelines(väljund)
    f.close()

