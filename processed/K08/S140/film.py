def loetleFilmid(zanr):
    f = open("filmid.txt", "r", encoding="UTF-8")
    filmid = []
    for rida in f:
        rida = rida.strip().split(" - ")
        if rida[1] == zanr:
            filmid += [rida[0]]
    f.close()
    return filmid
    
def lisaFilm(nimi, zanr):
    f = open("filmid.txt", "a", encoding="UTF-8")
    f.write(f'\n{nimi} - {zanr}')
    f.close()

def kustutaFilm(nimi):
    f = open("filmid.txt", "r", encoding="UTF-8")
    tekst = f.readlines()
    f.close()
    for i in tekst:
        if nimi in i:
            tekst.remove(i)
    f = open("filmid.txt", "w", encoding="UTF-8")
    for i in tekst:
        f.write(i)
    f.close()
