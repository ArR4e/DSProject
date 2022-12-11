import film

tähis = input("Tähis: ")
järjend= input("Järjend: ")

def töötleKäsk(tähis,järjend):
    while True:
        if tähis == "K":
            print("Võimalikud filmid on ",film.loetleFilmid(järjend))
            if film.loetleFilmid(järjend) == "[]":
                print("Soovitud žanriga filmi pole nimekirjas.")
            return True
        elif tähis == "L":
            film.lisaFilm(järjend)
            print("Film lisatud!")
            return True
        elif tähis == "V":
            print("Film nimekirjast kustutatud!")
            print("Head vaatamist!")
            film.kustutaFilm(järjend)
            return True
        else:
            return False
            break
