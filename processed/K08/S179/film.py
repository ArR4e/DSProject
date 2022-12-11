def loetleFilmid(zanr):
    f = open("filmid.txt","r",encoding="utf-8")
    filmid = []
    for rida in f:
        if zanr+"\n" == rida.split(" - ")[1]:
            filmid.append(rida.split(" - ")[0])
    f.close()
    return filmid

def lisaFilm(nimi,zanr):
    f = open("filmid.txt","a",encoding="utf-8")
    f.write(f"{nimi} - {zanr}\n")
    f.close()

def kustutaFilm(nimi):
    f = open("filmid.txt","r",encoding="utf-8")
    sisu = f.readlines()
    f.close()
    f = open("filmid.txt","w",encoding="utf-8")
    for i in sisu:
        if nimi != (i.split(" - ")[0]):
            f.write(i)
    f.close()

