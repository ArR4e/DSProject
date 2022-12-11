
def loetleFilmid(nimi):
    fail = open("filmid.txt", "r")
    jarj1 = []
    for film in fail:
        film1 = film.split("-")
        film1[1] = film1[1].strip()
        film1[0] = film1[0].strip()
        if film1[1] == nimi:
            jarj1 = jarj1 + [film1[0]]
    return (jarj1)
    fail.close()
    
#print(loetleFilmid("multikas"))
    
def lisaFilm(nimi, tuup):
    uld = nimi + " - " + tuup
    fail = open("filmid.txt", "r")
    failkont = fail.readline()
    fail.close()
    fail = open("filmid.txt", "a+")
    if len(failkont) != 0:
        fail.write("\n")
    fail.write(uld)
    fail.close()
    
#lisaFilm("Lotte","multikas")
    
def kustutaFilm(nimi):
    fail = open("filmid.txt", "r")
    jarj1 = []
    for film in fail:
        film1 = film.split("-")
        film1[1] = film1[1].strip()
        film1[0] = film1[0].strip()
        if film1[0] == nimi:
            continue
        jarj1 = jarj1 + [film]
    fail.close()
    fail = open("filmid.txt", "w")
    fail.write("")
    for el in jarj1:
        el = str(el)
        fail.write(el)
    fail.close()
    
        
#kustutaFilm("Shrek")