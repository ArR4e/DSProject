f = open("filmid.txt", encoding ="UTF-8")

a = [ ]

def loetleFilmid(zanr):
    for rida in f:
        if rida == " ":
            break
        jär = rida.split(" - ")
        if jär[1] == zanr:
            a.append(jär[0])
    return a

def lisaFilm(nimi, zanr):
    rida = nimi, "-", zanr
    f.write(rida)
    
    
def kustutaFilm(nimi):
    