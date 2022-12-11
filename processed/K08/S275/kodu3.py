import film

def töötleKäsk(x, y):
    if x == "K":
        for el in y:
            filmid = el
        a = film.loetleFilmid(filmid)
        if len(a) == 0:
            print("Filmid puuduvad")
        else:
            print("Võimalikud filmid on: ")
            for x in a:
                print(x)
    elif x == "L":
        lisa = " "
        for el in y:
           lisa = lisa + el
        film.lisaFilm(lisa, filmid)
    elif x == "V":
        vaata = " "
        for el in y:
            vaata = vaata + el
        if film.kustutaFilm(vaata) == True:
            print("Film nimekirjast kustutatud!\nHead vaatamist!")
        else:
            print("Ei")


print("Kuva filmid: K")
print("Lisa a:   L")
print("Vaata ai: V")
print("Lõpeta:      E")
