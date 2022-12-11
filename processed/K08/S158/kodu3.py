import film

def töötleKäsk(tähis, käsuargument) :
    if tähis == "K":
        f = film.loetleFilmid(käsuargument)
        print("Võimalikud filmid on:" + "\n" + str(f))
    elif tähis == "L":
        a = käsuargument[0]
        b = käsuargument[1]
        film.lisaFilm(a, b)
        print("Film lisatud!")
    elif tähis == "V":
        nimi = käsuargument
        film.kustutaFilm(nimi)
        print("Fail nimekirjast kustutatud." + "\n" + "Head vaatamist!")
    elif tähis == "E":
        return True
    else:
        return False
    
j = input("> ")
while True:
    if j[0] == "E":
        break
    else:
        töötleKäsk(j[0], j[1:])