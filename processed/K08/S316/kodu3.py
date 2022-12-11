import film

def töötleKäsk(tähis,käsuargument):
    if tähis == "K":
        f = film.loetleFilmid(käsuargument)
        print("Võimalikud filmid on: " + "\n" + str(f))
    elif tähis == "L":
        nimi = käsuargument[0]
        žanr = käsuargument[1]
        film.lisaFilm(nimi,žanr)
        print("Film lisatud!")
    elif tähis == "V":
        nimi = käsuargument
        film.kustutaFilm(nimi)
        print("Film nimekirjast kustutatud. Head vaatamist!")
    elif tähis == "E":
        return True
    else:
        return False


järjend = input("> ").split(" ")
while True:
    if järjend[0] == "E":
        break
    else:
        töötleKäsk(järjend[0],järjend[1:])
    järjend = input("> ").split(" ")
        