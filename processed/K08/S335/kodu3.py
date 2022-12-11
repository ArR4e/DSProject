import film
def töötleKäsk(a, b):
    if a == "K":
        valik = "\n".join(film.loetleFilmid(b[0]))
        if valik == "":
            return("Antud filmi ei ole nimekirjas.")
        else:
            return("Võimalikud filmid on: \n" + valik)
    elif a == "L":
        film.lisaFilm(b[0], b[1:])
        return("Film lisatud!")
    elif a == "V":
        film.kustutaFilm(b[0])
        return("Film nimekirjast kustutatud!\nHead vaatamist!")
    elif a == "E":
        return False
while True:
    käsk = (input("Sisesta valik: ")).split()
    if käsk == ["E"]:
        break
    täht = käsk[0]
    film1 = käsk[1:]
    print(töötleKäsk(täht, film1))