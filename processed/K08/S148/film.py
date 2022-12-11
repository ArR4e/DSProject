def loetleFilmid(zanr):
    j = []
    
    f = open("filmid.txt", encoding="UTF-8")
    for rida in f:
        rida = rida.strip()
        a = rida.split(" - ")
        
        if zanr == a[1]:
            j += [a[0]]
    f.close()
    
    return j

def lisaFilm(nimi, zanr):
    f = open("filmid.txt", "a", encoding="UTF-8")
    f.write("\n" + str(nimi) + " - " + str(zanr))
    f.close()

def kustutaFilm(nimi):
    j = ""
    f = open("filmid.txt", "r", encoding="UTF-8")
    for rida in f:
        a = rida.split(" - ")
        if nimi != a[0]:
            j += rida
    f.close()
    
    f = open("filmid.txt", "w", encoding="UTF-8")
    f.write(j.strip())
    f.close()